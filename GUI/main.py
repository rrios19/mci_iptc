####################################################################################
# Créditos a Khamisi Kibet de SpinnCode
# que elaboró una GUI con funcionalidades que se utilizan en el presente código
# Fuente: https://www.spinncode.com/designs/lNhoNaXE
########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
####################################################################################


import sys
import os
import re
import shutil
import json
import pandas as pd

from PySide2 import *

from IPTC_GUI_pyside import *

from qt_material import apply_stylesheet
import xml.etree.ElementTree as ET
from AuthWindow import AuthDialog
from ssh_connection import SshCommunication as ssh
import pyqtgraph as pg

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_IPTC()
        self.ui.setupUi(self)
        self.currentPathToWorkspace = ""
        self.currentWorkspaceName = ""
        self.currentlyOpenTest = ""
        self.ssh_link = ssh()
        #######################################################################
        ## # Remover la barra de título
        ########################################################################    
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        
        # Setup the plot widget
        self.graphWidget1 = pg.PlotWidget()
        self.ui.VlayGraph1.addWidget(self.graphWidget1)
        self.ui.Graph1.setLayout(self.ui.VlayGraph1)

        self.graphWidget2 = pg.PlotWidget()
        self.ui.VlayGraph2.addWidget(self.graphWidget2)
        self.ui.Graph2.setLayout(self.ui.VlayGraph2)

        self.graphWidget3 = pg.PlotWidget()
        self.ui.VlayGraph3.addWidget(self.graphWidget3)
        self.ui.Graph3.setLayout(self.ui.VlayGraph3)

        # Graph styling
        self.graphWidget1.setBackground('w')
        self.graphWidget2.setBackground('w')
        self.graphWidget3.setBackground('w')
        
        # Enable the plot legend
        self.graphWidget3.addLegend()

        # Data lists for each plot
        self.data1 = {'x': [], 'y': []}
        self.data2 = {'x': [], 'y': []}
        self.data3 = {'x': [], 'y1': [],'y2': [],'y3': [], 'y4': []}

        # Create a plot in the graph widget
        
        self.pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.plot1 = self.graphWidget1.plot(pen=self.pen)  # 'y' for yellow color
        self.plot2 = self.graphWidget2.plot(pen=self.pen)  # 'y' for yellow color
        self.plot3a = self.graphWidget3.plot(pen=self.pen, name = "Voltage (V)")  # 'y' for yellow color
        self.plot3b = self.graphWidget3.plot(pen='r', name = "Current (mA)")  # 'y' for yellow color
        self.plot3c = self.graphWidget3.plot(pen='b', name = "Resistance (Ohms)")  # 'y' for yellow color
        self.plot3d = self.graphWidget3.plot(pen='g', name = "Power (W)")  # 'y' for yellow color

        # Timer setup to refresh the graph
        self.timer = QTimer()
        self.timer.setInterval(2000)  # update every 2000 milliseconds (2 seconds)
        self.timer.timeout.connect(self.update_plots)
        self.timer.start()




        #######################################################################
        ## # Estilo efecto de sombra
        ########################################################################  
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 300, 550))


        

        #################################################################################
        # Window Size grip to resize window
        #################################################################################
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

       
        QSizeGrip(self.ui.size_grip)


        #######################################################################
        #Restablecer/Maximizar Ventana
        self.ui.maximize_btn.clicked.connect(lambda: self.restore_or_maximize_window())


        ##Cerrar Ventana
        self.ui.close_btn.clicked.connect(lambda: self.close())

        ##Minimizar Ventana
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())

        #######################################################################################
        ## Stacked Widget para New/Saved organization
        ## Establecer página de inicio por defecto
        self.ui.stackedWidgetWorkspace.setCurrentWidget(self.ui.home)

        #Cambiar a la página designada para espacio de trabajo guardado
        self.ui.selectWorkspaceBtn.clicked.connect(self.select_workspace)

        #Añadir file al treewidget
        self.ui.tests_recent_btn.clicked.connect(self.upload_recent)

        #Cargar una plantilla de prueba
        self.ui.template_2.clicked.connect(self.upload_template)
        


        #Cambiar a la página designada para espacio de nueva estación de trabajo
        self.ui.newWorkspaceBtn.clicked.connect(lambda: self.ui.stackedWidgetWorkspace.setCurrentWidget(self.ui.newWorkMenu))

        #Cambiar a la página designada resultados de BTM
        self.ui.BTMresBtn.clicked.connect(lambda: self.ui.stackedWidgetResGraphs.setCurrentWidget(self.ui.BTMres))

        #Cambiar a la página designada resultados de BTM
        self.ui.SAMresBtn.clicked.connect(lambda: self.ui.stackedWidgetResGraphs.setCurrentWidget(self.ui.SAMres))


        #Cambiar a la página designada resultados de BTM
        self.ui.VELMresBtn.clicked.connect(lambda: self.ui.stackedWidgetResGraphs.setCurrentWidget(self.ui.VELMres))

        #########################################################################################
        #Stacked Widget para las opciones de resultados
        self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt)



 

        #Selecciona frame de Interactive graphics
        self.ui.interacGraphBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.interactiveGrphOpt))

 

        #Selecciona frame de results comparison
        self.ui.resultCompBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.resCompOpt))

        #Selecciona frame de customize report
        self.ui.customReportBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.customRepOpt))


        self.ui.editNameBtn.clicked.connect(self.editFileName)


        # ###############################################
        # Función para mover la ventana cuando con el mouse en la barra de título
        # ###############################################

        def MoverVentana(e):
            # Detectar si la ventana es del tamaño normal
            # ###############################################  
            if self.isMaximized() == False: #Si no está maximizada
                # Mover ventana solo cuando se encuentra en tamaño normal  
                # ###############################################
                #Si el botón izquierdo del mouse se presiona (Solo aceptar clicks izquierdos)
                if e.buttons() == Qt.LeftButton:  
                    #Mover ventana
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                    
            if e.globalPos().y() <=20:
                self.showMaximized()
            else:
                self.showNormal()
        #######################################################################

        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.ui.project_info.mouseMoveEvent = MoverVentana
        #######################################################################



        ###################################################################################
        ###################################################################################
        # 
        #       SLIDE MENUS
        #
        #Develop and run tests toggle button
        self.ui.devBtnTest.clicked.connect(lambda: self.slideDownMenu(self.ui.slide_devtstmenu,self.ui.devBtnTest,800))
        self.ui.devBtnTest.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt))

        #Configure workspace toggle button
        self.ui.confWorkspaceBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.confWokspace_menu,self.ui.confWorkspaceBtn,800))
        self.ui.confWorkspaceBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt))

        #Data results toggle button
        self.ui.dataResultBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.dataResults_menu,self.ui.dataResultBtn,800))
        self.ui.dataResultBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt))        

        #Help toggle button
        self.ui.helpBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.help_menu,self.ui.helpBtn,800))
        self.ui.helpBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt)) 

        #Data results side menu toggle button
        self.ui.sideResultsBtn.clicked.connect(lambda: self.slideLeftMenu(self.ui.dataresult_sidemenu,self.ui.sideResultsBtn))

        #Develop and run tests side menu toggle button
        self.ui.side_btn_tests.clicked.connect(lambda: self.slideLeftMenu(self.ui.opt_menu,self.ui.side_btn_tests))


        #Develop and run tests side menu toggle button
        self.ui.newSeqBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.newSeq_slidemenu,self.ui.newSeqBtn,50))

        #Add members edit line
        self.ui.addMembersBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.addMembersLine,self.ui.addMembersBtn,800))
        #Creating new Organization

        self.ui.saveWorkspaceBtn.clicked.connect(lambda: self.save_new_workspace())

        ##Select Workspace options if workspace selected
        self.ui.workOptBtn.clicked.connect(lambda: self.ShowWorkspaceOptions())

        #Adding members
        self.ui.addBtn.clicked.connect(lambda: self.add_members())

        #Displaying ssh connection actions
        self.ui.ssh_connect_btn.clicked.connect(lambda: self.openSshControlMenu())

        #Add tests to queue

        self.ui.add2QueueBtn.clicked.connect(lambda: self.add_tests_to_queue())

        self.ui.ExcTestBtn.clicked.connect(lambda: self.execute_test())


        self.show()


    #Función para redimencionar la ventana

    def resizeWindow(self, e):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

   ########################################################################
    # Función  para deslizar menú
    ########################################################################
    def slideLeftMenu(self,sideMenu,sideMenuBtn):
        # Obtener ancho de la ventana de menu
        width = sideMenu.width()
        # Si está minimizado
        if width == 0:
            # Expandir Menú
            newWidth = 600

            sideMenuBtn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # Si está maximizado
        else:
            # Restablecer menu
            newWidth = 0
            sideMenuBtn.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))

        # Transición animada
        self.animation = QPropertyAnimation(sideMenu, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(100)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    #######################################################################
        
   ########################################################################
    # Función  para deslizar menú hacia abajo
    ########################################################################
    def slideDownMenu(self,slidedown_menu,btn,menu_height):
        # Obtener ancho de la ventana de menu
        height = slidedown_menu.height()
        # Si está minimizado
        menus = ["Develop and run tests","Configure Workspace","Data results","Help","Home"]
        if btn.text() in menus:
            homeMenuHeight = 0
            menus.remove(btn.text()) ##Elimina de las opciones el botón  que ha sido presionado
            if height == 0:  #Si los menús restantes están minimizados les asigna un ícono
                for menu in menus:     
                    if menu == "Develop and run tests":
                        frame = self.ui.slide_devtstmenu
                        actBtn = self.ui.devBtnTest
                        actBtnIconPath = u":/icons/icons/battery-charging.svg"
                    elif menu == "Configure Workspace":
                        frame = self.ui.confWokspace_menu
                        actBtn = self.ui.confWorkspaceBtn
                        actBtnIconPath = u":/icons/icons/settings.svg"
                    elif menu == "Data results":
                        frame = self.ui.dataResults_menu
                        actBtn = self.ui.dataResultBtn
                        actBtnIconPath = u":/icons/icons/bar-chart-2.svg"
                    elif menu == "Help":
                        frame = self.ui.help_menu
                        actBtn = self.ui.helpBtn
                        actBtnIconPath = u":/icons/icons/help-circle.svg"
                    else:
                        frame = self.ui.home_frame


                    if frame.height() > 0: #De los menús restantes hay alguno que esté desplegado,
                        frame.setMaximumHeight(0) #Si lo hay, lo minimiza
                        if menu != "Home":
                            actBtn.setIcon(QtGui.QIcon(actBtnIconPath)) #Y coloca el ícono inicial

                # Expandir el menú deseado
                newHeight = menu_height
            
                btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-up.svg"))
            # Si está maximizado
            else:
                # Restablecer menu
                if btn.text() == "Develop and run tests":
                    btnIconPath = u":/icons/icons/battery-charging.svg"
                elif btn.text() == "Configure Workspace":
                    btnIconPath = u":/icons/icons/settings.svg"
                elif btn.text() == "Data results":
                    btnIconPath = u":/icons/icons/bar-chart-2.svg"
                elif btn.text() == "Help":
                    btnIconPath = u":/icons/icons/help-circle.svg"
                else:
                    btnIconPath = u":/icons/icons/align-center.svg"
                newHeight = 0
                homeMenuHeight = 400
                btn.setIcon(QtGui.QIcon(btnIconPath))
                
        else:
            if height == 0:
                newHeight = menu_height

            else:
                newHeight = 0

        # Transición animada
        self.animation = QPropertyAnimation(slidedown_menu, b"maximumHeight")#Anima minimumWidht
        self.animation.setDuration(100)
        self.animation.setStartValue(height)#El valor inicial el alto actual del menú
        self.animation.setEndValue(newHeight)#El ancho final es el nuevo valor de altura
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        self.ui.home_frame.setMaximumHeight(homeMenuHeight)
    #######################################################################



    #######################################################################
    # Añadir eventos del mouse a la ventana
    #######################################################################
    def mousePressEvent(self, event):
        # ###############################################
        # Obtener posición actual del mouse
        self.clickPosition = event.globalPos()
        # Se utiliza el valor cuando la ventana se mueve
    #######################################################################
    #######################################################################

    #######################################################################
    # Actualizar el ícono del botón de restabler cuando la ventana es maximizada o minimizada
    #######################################################################
    def restore_or_maximize_window(self):
        # Si la ventana está maximizada
        if self.isMaximized():
            self.showNormal()
            # Cambiar ícono
            self.ui.maximize_btn.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            # Cambiar ícono
            self.ui.maximize_btn.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))


    #########################################################################
    #Guardar un  nuevo Workspace
    #########################################################################
    def save_new_workspace(self):
        name = self.ui.line_name.text()
        org = self.ui.line_org.text()
        team = self.ui.line_team.text()

    
        self.currentWorkspaceName = name
        parentDir = os.getcwd()
        pathToWorkspace = os.path.join(parentDir, name)

        if os.path.exists(pathToWorkspace):
            QMessageBox.warning(self, "Warning", f"{name} workspace already exists, try using another name.")
        else:
            self.currentPathToWorkspace = pathToWorkspace
            os.mkdir(pathToWorkspace)
            pathWorkspaceResults = os.path.join(pathToWorkspace, "results")
            os.mkdir(pathWorkspaceResults)
            pathDevnRunTest = os.path.join(pathToWorkspace, "develop_and_run_tests")
            os.mkdir(pathDevnRunTest)
            pathConfigure = os.path.join(pathToWorkspace, "configuration")
            os.mkdir(pathConfigure)
            # Create a QFont object with the desired font family and size
            font = QFont("Times New Roman", 10)  # Example: Times New Roman font, 10pt size

            # Apply the font to the label
            self.ui.label_working_path.setFont(font)
            self.ui.label_working_path.setText(f"<b><div align='center'>Workspace:<br><i>{name}</i></div></b>") # Update the label text
            
            with open(f"{pathToWorkspace}/Workspace_Info.txt", "w") as file:
                file.write(f"Name:{name}\n")
                file.write(f"Organization:{org}\n")
                file.write(f"Team:{team}\n")
                file.close()

            # Create a hidden .iptc file as a valid workspace identifier
            with open(os.path.join(pathToWorkspace, ".iptc"), "w") as iptc_file:
                iptc_file.write("This is a valid IPTC workspace")

            QMessageBox.information(self, "InformatioQPixmap(n", f"{name} workspace created successfully")
            self.ui.line_name.clear()
            self.ui.line_org.clear()
            self.ui.line_team.clear()

    #Función para desplegar las opciones del Workspace si un ha sido seleccionado
    def ShowWorkspaceOptions(self):

        if self.currentPathToWorkspace != "":
            self.ui.stackedWidgetWorkspace.setCurrentWidget(self.ui.saveWorksMenu)
        else:

            QMessageBox.warning(self, "Warning", "No workspace has been loaded or created, please select or create one first")

    # Función para seleccionar entre workspaces guardados
    def select_workspace(self):
        self.ui.stackedWidgetWorkspace.setCurrentWidget(self.ui.home)
        options = QFileDialog.Options() 
        selected_folder = QFileDialog.getExistingDirectory(self, "Select Workspace","", options=options)

        if selected_folder:
            # Revisa si el folder seleccionado contiene el archivo .iptc
            iptc_file_path = os.path.join(selected_folder, ".iptc")
            if os.path.exists(iptc_file_path):
                self.currentPathToWorkspace = selected_folder
                
                workspaceInfoPath = os.path.join(selected_folder,"Workspace_Info.txt")
                with open(workspaceInfoPath,"r") as workspaceInfo:
                    self.currentWorkspaceName = workspaceInfo.readlines()[0].split(":")[1].split('\n')[0]
                    workspaceInfo.close()

                # Create a QFont object with the desired font family and size
                font = QFont("Times New Roman", 10)  # Example: Times New Roman font, 10pt size

                # Apply the font to the label
                self.ui.label_working_path.setFont(font)
                self.ui.label_working_path.setText(f"<b><div align='center'>Workspace:<br><i>{self.currentWorkspaceName}</i></div></b>")  # Update the label text with the selected folder
                workspaceInfo.close()
                QMessageBox.information(self, "Information", "Workspace selected successfully")
            else:
                QMessageBox.warning(self, "Warning", "Selected folder is not a valid workspace")


    #Function to open recently open directory
    def upload_recent(self):
        options = QFileDialog.Options()
        selected_file, _ = QFileDialog.getOpenFileName(self, "Select XML File", "", "XML Files (*.xml)", options=options)
        self.upload_xml_to_tree_widget(selected_file)


    #Function to upload a template .xml file
        
    def upload_template(self):
        options = QFileDialog.Options()
        initialDir = os.path.expanduser('~')
        selected_file, _ = QFileDialog.getOpenFileName(self, "Select XML File", initialDir, "XML Files (*.xml)", options=options)
        self.upload_xml_to_tree_widget(selected_file)

    #Function to add the "change name" functionality to the test



    def editFileName(self):
        new_filename, ok = QInputDialog.getText(self, "Change File Name", "Enter new file name:", text=self.ui.filenameLabel.text())
        if ok and new_filename.split(".")[1] == "xml":
            old_path = f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}'
            self.ui.filenameLabel.setText(new_filename)
            self.currentlyOpenTest = new_filename
            new_path = f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}'


            # Copy the file with a different name
            shutil.copy(old_path, new_path)

            # If the old file is different and exists, remove it
            if old_path != new_path and os.path.exists(old_path):
                os.remove(old_path)
        else:
            QMessageBox.warning(self, "warning","Unknown file format, only XML files are allowed")

    # Function to upload to the xml_tree
    def upload_xml_to_tree_widget(self, selected_file):
        if self.currentPathToWorkspace != "":
            filename = os.path.basename(selected_file)
            self.currentlyOpenTest = filename
            if selected_file:
                # Clear existing items in the tree widget
                self.ui.treeWidget.setHeaderHidden(True)
                self.ui.treeWidget.clear()
                self.ui.treeWidget.setMaximumSize(16777215,16777215)
                self.ui.treeWidget.setColumnWidth(0, 250)  # Set the width of the first column to 200 pixels
                self.ui.treeWidget.setColumnWidth(1,250)  # Adjust as necessary for your content
                
                
                try:
                    #Function to verify the name given to children or attributes
                    def is_valid_tag(tag_name):
                        return re.match("^[A-Za-z][\w.-]*$", tag_name) is not None

                    save_test_copy_path = os.path.join(self.currentPathToWorkspace,'develop_and_run_tests',self.currentlyOpenTest)
                    # Copy the file
                    if save_test_copy_path != selected_file:
                        shutil.copy(selected_file, save_test_copy_path)

                    # Parse the XML file
                    tree = ET.parse(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}')
                    root = tree.getroot()
                    
                    # Set the column count of the tree widget
                    self.ui.treeWidget.setColumnCount(2)
                    
                    #self.ui.treeWidget.setHeaderHidden(True)
                    #self.ui.treeWidget.setHeaderLabels(["File", filename])

                    # Add the root item to the tree widget
                    root_item = QTreeWidgetItem([root.tag])
                    self.ui.treeWidget.addTopLevelItem(root_item)

                    # Store the associated xml_element with the tree widget item for the root
                    root_item.setData(0, Qt.UserRole, root)

                        

                    def add_items(parent_item, xml_element):
                        for child in xml_element:
                            child_item = QTreeWidgetItem([child.tag])
                            parent_item.addChild(child_item)
                            
                            # Store the associated xml_element with the tree widget item
                            child_item.setData(0, Qt.UserRole, child)
                            
                            # Add attributes as children of the element item
                            for attr_name, attr_value in child.attrib.items():
                                attr_item = QTreeWidgetItem([f"@{attr_name}", attr_value])
                                child_item.addChild(attr_item)

                            # Recursively add child elements
                            add_items(child_item, child)

                            # Add text content, if present and not just whitespace
                            if child.text and not child.text.isspace():
                                content_item = QTreeWidgetItem(["Value", child.text.strip()])
                                child_item.addChild(content_item)

                    # Populate the tree widget with XML data
                    add_items(root_item, root)

                    

                    # Function to add a new child element
                    def add_child_element():
                        selected_item = self.ui.treeWidget.currentItem()
                        if selected_item is not None:
                            valid = False
                            while not valid:
                                xmlElement = selected_item.data(0, Qt.UserRole)  # Retrieve the associated XML element
                                new_element_name, ok = QInputDialog.getText(self, "Add Child Element", "Enter the name of the new element:")
                                
                                if ok:
                                    if is_valid_tag(new_element_name):
                                        valid = True
                                        new_element = ET.SubElement(xmlElement, new_element_name)  # Create and append the new element
                                        
                                        
                                        new_element.text = ""  # Set text for the new element
                                        # Reflect the changes in the QTreeWidget
                                        new_item = QTreeWidgetItem([new_element.tag])
                                        selected_item.addChild(new_item)
                                        
                                        if new_element.text:
                                            value_item = QTreeWidgetItem(["Value", new_element.text])
                                            new_item.addChild(value_item)
                                        
                                        # Update the association for the new QTreeWidgetItem
                                        new_item.setData(0, Qt.UserRole, new_element)
                                        
                                        # Write changes to the file
                                        tree.write(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}', encoding="utf-8", xml_declaration=True)
                                    else:
                                        QMessageBox.warning(self, "Invalid Tag", "The tag name is invalid. Please enter a valid tag name without spaces.")
                                else:
                                    break
                                    

                    def add_attribute():
                        selected_item = self.ui.treeWidget.currentItem()
                        if selected_item is not None:
                            xmlElement = selected_item.data(0, Qt.UserRole)  # Retrieve the associated XML element
                            
                            if xmlElement is not None:
                                attribute_name, ok = QInputDialog.getText(self, "Add Attribute", "Enter the name of the new attribute:")
                                if ok and attribute_name:
                                    attribute_value, ok = QInputDialog.getText(self, "Set Attribute Value", "Enter the value for the new attribute:")
                                    if ok:
                                        xmlElement.set(str(attribute_name), attribute_value)  # Set attribute for the element
                                        
                                        # Update the QTreeWidgetItem display
                                        newAttr = QTreeWidgetItem([f"@{attribute_name}",attribute_value])
                                        selected_item.addChild(newAttr)

                                        
                                        # Optionally: Write changes back to XML file
                                        tree.write(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}', encoding='utf-8', xml_declaration=True)

                                        # Note: 'tree' should be accessible here, which might require you to manage the ElementTree object's scope appropriately.

                    def remove_attribute():
                        selected_item = self.ui.treeWidget.currentItem()
                        if selected_item is not None:
                            # Check if the selected item is an attribute
                            if selected_item.text(0).startswith("@"):
                                # Get the parent item and its associated XML element
                                parent_item = selected_item.parent()
                                xmlElement = parent_item.data(0, Qt.UserRole)
                                if xmlElement is not None:
                                    # Extract attribute name and remove '@' prefix
                                    attribute_name = selected_item.text(0)[1:]
                                    # Remove the attribute from the XML element
                                    if xmlElement.get(attribute_name) is not None:
                                        xmlElement.attrib.pop(attribute_name, None)
                                        # Remove the attribute item from the tree
                                        parent_item.removeChild(selected_item)
                                        
                                        # Optionally: Write changes back to XML file
                            tree.write(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}', encoding='utf-8', xml_declaration=True)

                    # Function to modify the value of an element
                    def modify_element_value():
                        selected_item = self.ui.treeWidget.currentItem()
                        if selected_item is not None:
                            item_text = selected_item.text(0)
                            new_value, ok = QInputDialog.getText(self, "Modify Value", "Enter the new value:")

                            if ok:
                                if item_text.startswith("@"):  # This item represents an attribute
                                    attr_name = item_text[1:]  # Extract attribute name
                                    parent_item = selected_item.parent()
                                    parent_element_tag = parent_item.text(0)
                                    parent_element = tree.find(f".//{parent_element_tag}")
                                    if parent_element is not None:
                                        parent_element.set(attr_name, new_value)
                                        selected_item.setText(1, new_value)  # Update GUI

                                elif item_text == "Value":  # This item represents element text content
                                    parent_item = selected_item.parent()
                                    parent_element_tag = parent_item.text(0)
                                    parent_element = tree.find(f".//{parent_element_tag}")
                                    if parent_element is not None:
                                        parent_element.text = new_value
                                        selected_item.setText(1, new_value)  # Update GUI
                        tree.write(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}', encoding="utf-8", xml_declaration=True)
                        
                    def remove_child():
                        selected_item = self.ui.treeWidget.currentItem()
                        if selected_item is None:
                            return  # No selection made
                        
                        parent_item = selected_item.parent()
                        xml_element = selected_item.data(0, Qt.UserRole)
                        parent_xml_element = parent_item.data(0, Qt.UserRole) if parent_item else None

                        if xml_element is not None:
                            # Remove from the XML structure
                            if parent_xml_element is not None:
                                parent_xml_element.remove(xml_element)
                            else:
                                # Assuming xml_element is a top-level element in this case
                                self.xml_root.remove(xml_element)  # xml_root is your XML document's root element
                                
                            # Remove from the QTreeWidget
                            if parent_item is None:  # If it's a top-level item
                                self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(selected_item))
                            else:
                                parent_item.removeChild(selected_item)

                        tree.write(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}', encoding="utf-8", xml_declaration=True)

                    def remove_attribute():
                        selected_item = self.ui.treeWidget.currentItem()
                        if selected_item is not None:
                            # Check if the selected item is an attribute
                            if selected_item.text(0).startswith("@"):
                                # Get the parent item and its associated XML element
                                parent_item = selected_item.parent()
                                xmlElement = parent_item.data(0, Qt.UserRole)
                                if xmlElement is not None:
                                    # Extract attribute name and remove '@' prefix
                                    attribute_name = selected_item.text(0)[1:]
                                    # Remove the attribute from the XML element
                                    if xmlElement.get(attribute_name) is not None:
                                        xmlElement.attrib.pop(attribute_name, None)
                                        # Remove the attribute item from the tree
                                        parent_item.removeChild(selected_item)
                                        
                                        # Optionally: Write changes back to XML file
                                        tree.write(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}', encoding='utf-8', xml_declaration=True)

                    def openMenu(position):
                        selected_item = self.ui.treeWidget.itemAt(position)
                        if selected_item is None:
                            return

                        menu = QMenu()
                        
                        ## Los atributos de los elementos tienen en su texto un @
                        ## con eso se diferencian.

                        if "@" in selected_item.text(0):
                            #Cuando sólo es atributo no es solo es posible modificar su valor

                            modify_attribute_value = menu.addAction("Modify Value")
                            modify_attribute_value.triggered.connect(modify_element_value)

                            action_remove_attr = menu.addAction("Remove Attribute")
                            action_remove_attr.triggered.connect(remove_attribute)
                            
                        else:
                            #Si es hijo o padre sí es posible agregar un hijo o un atributo al mismo

                            action_remove_child = menu.addAction("Remove Child")
                            action_remove_child.triggered.connect(remove_child)

                            action_add_child = menu.addAction("Add Child")
                            action_add_child.triggered.connect(add_child_element)
                        
                            action_add_attribute = menu.addAction("Add Attribute")
                            action_add_attribute.triggered.connect(add_attribute)
                        
                        menu.exec_(self.ui.treeWidget.viewport().mapToGlobal(position))

                    ##################################################
                    # Add metadata
                    ##################################################
                    MdataItems = ['Authors','Organization']
                    for Mdata_item in MdataItems:
                        item_queue = [self.ui.treeWidget.topLevelItem(i) for i in range(self.ui.treeWidget.topLevelItemCount())]
                        while item_queue:
                            current_item = item_queue.pop(0)
                            if current_item.text(0) == Mdata_item:
                                selected_item = current_item
                                break
                            else:
                                for i in range(current_item.childCount()):
                                    item_queue.append(current_item.child(i))
                        xmlElement = selected_item.data(0, Qt.UserRole)  # Retrieve the associated XML element
                        if Mdata_item == "Authors":
                            with open(os.path.join(self.currentPathToWorkspace,'Team_Members.txt'),'r') as Authors:
                                AuthorsData = Authors.readlines()
                            
                            author_cnt = 1
                            for author in AuthorsData:
                                authorName = author.split('\n')[0]
                                if xmlElement is not None:
                                    attribute_name = f'Author_{author_cnt}'

                                    author_cnt += 1

                                    attribute_value = authorName
                                    xmlElement.set(str(attribute_name), attribute_value)  # Set attribute for the element
                                    
                                    # Update the QTreeWidgetItem display
                                    newAttr = QTreeWidgetItem([f"@{attribute_name}",attribute_value])
                                    selected_item.addChild(newAttr)
                                    # Optionally: Write changes back to XML file
                                    tree.write(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}', encoding='utf-8', xml_declaration=True) 
                        else:
                            with open(os.path.join(self.currentPathToWorkspace,'Workspace_Info.txt'),'r') as WorkspaceInfo: 
                                OrgName = WorkspaceInfo.readlines()[1].split(':')[1].split('\n')[0]
                                WorkspaceInfo.close()

                            if xmlElement is not None:
                                attribute_name = 'Organization'
                                attribute_value = OrgName
                                xmlElement.set(str(attribute_name), attribute_value)  # Set attribute for the element
                                
                                # Update the QTreeWidgetItem display
                                newAttr = QTreeWidgetItem([f"@{attribute_name}",attribute_value])
                                selected_item.addChild(newAttr)
                                # Optionally: Write changes back to XML file
                                tree.write(f'{self.currentPathToWorkspace}/develop_and_run_tests/{self.currentlyOpenTest}', encoding='utf-8', xml_declaration=True) 
                     
                

                    
                    # Enable context menu and connect signal
                    self.ui.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
                    self.ui.treeWidget.customContextMenuRequested.connect(openMenu)
                    
                    
                    

                    QMessageBox.information(self, "Success", "XML data loaded successfully into the tree widget.")

                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to parse XML file: {str(e)}")

            self.ui.TestActionsFrame.setMaximumHeight(50)
            self.ui.filenameLabel.setText(self.currentlyOpenTest)
            self.ui.TestNameFrame.setMaximumHeight(50)
            #Change the test file name 
            

        else:
            QMessageBox.warning(self, 'Warning','Please select a workspace before you attempt to create or load a test')

    #Función para enviar tests a la Raspberry y añadirlos a la cola
                
    def add_tests_to_queue(self):
        
        if self.ssh_link.connected:
            if self.currentPathToWorkspace != "":   
                try:
                    ##EXECUTED IN RASPBERRY PI
                    ##Create a IPTC directory to store all the app's data
                    #Create self.currentPathToWorkspace} and tests (within workspace) directories   
                    result = self.ssh_link.execute_command(['touch file_dir_check.txt',f'echo IPTC/{self.currentWorkspaceName}/tests/queued_tests.txt > file_dir_check.txt','python3 file_check.py'])


                    ##Send the actual testfile
                    result,flag = self.ssh_link.send_file(self.currentPathToWorkspace+f'/develop_and_run_tests/{self.currentlyOpenTest}',f'IPTC/{self.currentWorkspaceName}/tests/{self.currentlyOpenTest}',self.currentlyOpenTest)
                    if not flag:
                        QMessageBox.information(self, "Success", f"{result} and added to queue")

                    else:
                        QMessageBox.warning(self, "Warning", result)
                        return
                        
                    result = self.ssh_link.execute_command([f"echo {self.currentlyOpenTest} >> IPTC/{self.currentWorkspaceName}/tests/queued_tests.txt"])

                except:
                    QMessageBox.warning(self, "Warning", result)
            else:
                QMessageBox.warning(self, "Warning", f"No workspace has been selected, please choose a workspace to save the tests results")
        else:
            QMessageBox.warning(self, "Warning", f"An ssh connection must be established first, please select a device and then send the test")

    def execute_test(self):
        if self.ssh_link.connected:
            try:
                result = self.ssh_link.execute_command(['python3 module_handler.py'])

            except:
                QMessageBox.warning(self, "Warning", result)


        else:
            QMessageBox.warning(self, "Warning", f"An ssh connection must be established first, please select a device, send the test and execute it")





    def update_plots(self):
            self.graphWidget1.setLabel('left', 'Voltage', units='V')
            self.graphWidget1.setLabel('bottom', 'Time', units='s')
            self.graphWidget2.setLabel('left', 'Voltage', units='V')
            self.graphWidget2.setLabel('bottom', 'Current', units='mA')
            self.graphWidget3.setLabel('bottom', 'Time', units='s')
        


            # This function needs to be modified to handle reading each dataset correctly
            try:
                if os.path.exists(f'{self.currentPathToWorkspace}/results/'):
                    # Read new data for each graph from separate CSVs
                    data1 = pd.read_csv(f'{self.currentPathToWorkspace}/results/BTM.csv')
                    data2 = pd.read_csv(f'{self.currentPathToWorkspace}/results/SAM.csv')
                    data3 = pd.read_csv(f'{self.currentPathToWorkspace}/results/VELM.csv')

                    # Append data for each graph
                    self.data1['x'] = data1['Time(s)']
                    self.data1['y'] = data1['Voltage(V)']
                    self.data2['x'] = data2['Current(mA)']
                    self.data2['y'] = data2['Voltage(V)']

                    self.data3['x'] = data3['Time(s)']
                    self.data3['y1'] = data3['Voltage(V)']
                    self.data3['y2'] = data3['Current(mA)']
                    self.data3['y3'] = data3['Resistance(Ohms)']
                    self.data3['y4'] = data3['Power(W)']

                    # Update each plot
                    self.plot1.setData(self.data1['x'], self.data1['y'])
                    self.plot2.setData(self.data2['x'], self.data2['y'])
                    self.plot3a.setData(self.data3['x'], self.data3['y1'])
                    self.plot3b.setData(self.data3['x'], self.data3['y2'])
                    self.plot3c.setData(self.data3['x'], self.data3['y3'])
                    self.plot3d.setData(self.data3['x'], self.data3['y4'])

            except Exception as e:
                print(f"An error occurred: {e}")


    ##########################################################
    ##          
    ##  Función para establecer conexión con la rasp
    ##
    ##########################################################
    def openSshControlMenu(self):
        menu = QMenu()
        

        if self.ssh_link.connected:

            end_com = menu.addAction("Close connection")
            end_com.triggered.connect(self.ssh_close_connection)
            
        else:
            establish_link = menu.addAction("Link device")
            establish_link.triggered.connect(self.ssh_connect)
        
        menu.exec_(self.ui.ssh_connect_btn.mapToGlobal(self.ui.ssh_connect_btn.pos()))


    def ssh_connect(self):

        if self.currentPathToWorkspace != "":
            no_error = False  ##Booleano para definir un ciclo para obtener valor de hostname

            ## HOSTNAME

            #Loops until it gets a correct format for the hostname
            while not no_error:
                #Ask for Rpi hostname
                rpi_hostname, ok_hostname = QInputDialog.getText(self, "SSH Login", "Please enter your hostname (IP address):")
                if ok_hostname == QInputDialog.Accepted:
                    try:
                        self.ssh_link.hostname = rpi_hostname
                        no_error = True
                    except ValueError as HostError:
                        QMessageBox.warning(self, "Warning", str(HostError))
                else:
                    break

            if self.ssh_link.hostname != "":
                no_error = False
                ## USERNAME
                #Ask for Rpi username
                while not no_error:
                    rpi_username, ok_username = QInputDialog.getText(self, "SSH Login", "Please enter your username:")
                    
                    if ok_username == QInputDialog.Accepted:
                        try:
                            self.ssh_link.username = rpi_username
                            no_error = True
                        except ValueError as UsernameError:
                            QMessageBox.warning(self, "Warning", str(UsernameError))
                    else:
                        break

                if self.ssh_link.username != "":
                    ## PASSWORD or PRIVATE KEY LOCATION

                    ##Abrir ventana de dialogo para selección de autenticación ssh
                    dialog = AuthDialog(self)
                    result = dialog.exec_()
                    if result == QDialog.Accepted:
                        try:
                            self.ssh_link.passwd_auth = dialog.passwd_auth
                            #print(f"Dialog Accepted, {dialog.selected_method} authentication was selected")
                        except ValueError as AuthError:
                            QMessageBox.warning(self, "Warning", str(AuthError))
                    else:
                        QMessageBox.warning(self, "Warning", "An authentication method must be selected to establish connection")

                    if self.ssh_link.passwd_auth:
                        rpi_password, ok_password = QInputDialog.getText(self, "SSH Login", "Please enter your password:", QLineEdit.Password)
                        if ok_password == QInputDialog.Accepted:
                            status = self.ssh_link.connect(rpi_password)

                        else: 
                            QMessageBox.warning(self, "Warning", f"Password requred to log in")
                    else:
                        ssh_dir = os.path.expanduser('~/.ssh') # Default private key location
                        private_key_path = os.path.join(ssh_dir, f'id_rsa')
                        public_key_path = f'{private_key_path}.pub'

                        # Check if both the private and public keys exist
                        private_key_exists = os.path.isfile(private_key_path)
                        public_key_exists = os.path.isfile(public_key_path)

                        if not (private_key_exists or public_key_exists):
                            private_key_path, ok_username = QInputDialog.getText(self, "SSH Login", "Please enter path to your ssh private key directory:")
                        
                        status = self.ssh_link.connect(private_key_path)

                    ##Revisa la conexión para actualizar símbolos y etiquetas

                    if self.ssh_link.connected:
                        self.ui.ssh_connect_btn.setIcon(QtGui.QIcon(u":/icons/icons/zap.svg"))
                        self.ui.connectLabel.setText(f"Connected to <b>{self.ssh_link.username}</b>")
                        self.ui.connectionStatus.setMaximumHeight(500)
                        QMessageBox.information(self, "Success", status)
                        


                        
                        #Execute the script that verifies and creates directory if it does no exits.

                    else:
                        self.ui.ssh_connect_btn.setIcon(QtGui.QIcon(u":/icons/icons/zap-off.svg"))
                        QMessageBox.warning(self, "Warning", status)
                        self.ui.connectLabel.setText("")
                        self.ui.connectionStatus.setMaximumHeight(0)      

        else:
            QMessageBox.warning(self, "Warning", "A workspace must be selected or created before you attempt to connect")



    #Función para cerrar conexión ssh
    def ssh_close_connection(self):
        if self.ssh_link.connected:
            currentUser = self.ssh_link.username
            close_msg = self.ssh_link.close_connection()
            if self.ssh_link.connected:
                QMessageBox.warning(self, "Warning", close_msg)
            else:
                self.ui.ssh_connect_btn.setIcon(QtGui.QIcon(u":/icons/icons/zap-off.svg"))
                self.ui.connectLabel.setText("")
                self.ui.connectionStatus.setMaximumWidth(0)
                QMessageBox.information(self, "Information", f"Connection closed with <b>{currentUser}</b>")
                currentUser = ''

        else:
            QMessageBox.warning(self, "Warning", f"No ssh connection has been established yet")

    


    #########################################################################
    #Guardar añadir nuevos miembros
    #########################################################################
    def add_members(self):
        newMember = self.ui.line_newMember.text()
        with open(f"{self.currentPathToWorkspace}/Team_Members.txt", "a+") as f:
            f.seek(0)
            members = f.readlines()
            duplicateFlag = False
            for member in members:
                realmember = member.split("\n")[0]
                if realmember == newMember:
                    duplicateFlag = True
                    break
                else:
                    duplicateFlag = False
        
            if duplicateFlag:
                QMessageBox.warning(self, "Warning", f"The name {newMember} is already part of the team")
            else:
                f.write(f"{newMember}\n")
                f.close()
                QMessageBox.information(self, "Information", f"{newMember} added succesfully to the team")
                self.ui.line_newMember.clear()

if __name__ == "__main__":
    iptc = QApplication(sys.argv)
    iptc_window = VentanaPrincipal()
    apply_stylesheet(iptc,theme='light_blue.xml', invert_secondary=True)
    sys.exit(iptc.exec_())

