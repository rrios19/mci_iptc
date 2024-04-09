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

from PySide2 import *

from IPTC_GUI_pyside import *

from qt_material import apply_stylesheet
import xml.etree.ElementTree as ET
from AuthWindow import AuthDialog
from ssh_connection import SshCommunication as ssh
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_IPTC()
        self.ui.setupUi(self)
        self.currentPathToWorkspace = ""
        self.ssh_link = ssh()
        #######################################################################
        ## # Remover la barra de título
        ########################################################################    
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 


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
        self.ui.selectWorkspaceBtn.clicked.connect(self.select_workspace_and_change_widget)

        #Añadir file al treewidget
        self.ui.tests_recent_btn.clicked.connect(self.upload_recent)

        #Cargar una plantilla de prueba
        self.ui.template_2.clicked.connect(self.upload_template)
        


        #Cambiar a la página designada para espacio de nueva estación de trabajo
        self.ui.newWorkspaceBtn.clicked.connect(lambda: self.ui.stackedWidgetWorkspace.setCurrentWidget(self.ui.newWorkMenu))

        #########################################################################################
        #Stacked Widget para las opciones de resultados
        self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt)

        #Selecciona frame de integrated analysis
        self.ui.intAnalysisBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.intAnalysisOpt))

        #Selecciona frame de Filters, Tags and Groups
        self.ui.filTagsGrBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.ftgOpt))

        #Selecciona frame de Interactive graphics
        self.ui.interacGraphBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.interactiveGrphOpt))

        #Selecciona frame de pattern and anomaly detection
        self.ui.patAnoDetBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.pandAnomDetOpt))

        #Selecciona frame de results comparison
        self.ui.resultCompBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.resCompOpt))

        #Selecciona frame de customize report
        self.ui.customReportBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.customRepOpt))

        #Establece la conexión ssh con la raspberry pi
        self.ui.linkDeviceBtn.clicked.connect(lambda: self.ssh_connect())

        #Función para enviar pruebas a la cola

        self.ui.add2QueueBtn.clicked.connect(lambda: self.add_tests_to_queue())

        #Corta la comunicación ssh con la Raspberry pi

        self.ui.closeCntBtn.clicked.connect(lambda: self.ssh_close_connection())
        
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

        #Adding members
        self.ui.addBtn.clicked.connect(lambda: self.add_members())


        self.show()




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
        self.animation.setDuration(250)
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
        menus = ["Develop and run tests","Configure Workspace","Data results","Help"]
        if btn.text() in menus:
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
                    else:
                        frame = self.ui.help_menu
                        actBtn = self.ui.helpBtn
                        actBtnIconPath = u":/icons/icons/help-circle.svg"

                    if frame.height() > 0: #De los menús restantes hay alguno que esté desplegado,
                        frame.setMaximumHeight(0) #Si lo hay, lo minimiza
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
                btn.setIcon(QtGui.QIcon(btnIconPath))
        else:
            if height == 0:
                newHeight = menu_height

            else:
                newHeight = 0

        # Transición animada
        self.animation = QPropertyAnimation(slidedown_menu, b"maximumHeight")#Anima minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(height)#El valor inicial el alto actual del menú
        self.animation.setEndValue(newHeight)#El ancho final es el nuevo valor de altura
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
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

        parentDir = os.getcwd()
        pathToWorkspace = os.path.join(parentDir, name)

        if os.path.exists(pathToWorkspace):
            QMessageBox.warning(self, "Warning", f"{name} workspace already exists, try using another name.")
        else:
            self.currentPathToWorkspace = pathToWorkspace
            os.mkdir(pathToWorkspace)
            pathWorkspaceResults = os.path.join(pathToWorkspace, "results")
            os.mkdir(pathWorkspaceResults)
            pathDevnRunTest = os.path.join(pathToWorkspace, "develop and run test")
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

            QMessageBox.information(self, "Information", f"{name} workspace created successfully")
            self.ui.line_name.clear()
            self.ui.line_org.clear()
            self.ui.line_team.clear()

    def select_workspace_and_change_widget(self):
        self.select_workspace()
        self.ui.stackedWidgetWorkspace.setCurrentWidget(self.ui.saveWorksMenu)

    # Función para seleccionar entre workspaces guardados
    def select_workspace(self):
        options = QFileDialog.Options() 
        selected_folder = QFileDialog.getExistingDirectory(self, "Select Workspace","", options=options)

        if selected_folder:
            # Revisa si el folder seleccionado contiene el archivo .iptc
            iptc_file_path = os.path.join(selected_folder, ".iptc")
            if os.path.exists(iptc_file_path):
                self.currentPathToWorkspace = selected_folder
                
                workspaceInfoPath = os.path.join(selected_folder,"Workspace_Info.txt")
                with open(workspaceInfoPath,"r") as workspaceInfo:
                    WorkspaceName = workspaceInfo.readlines()[0].split(":")[1]
                

                # Create a QFont object with the desired font family and size
                font = QFont("Times New Roman", 10)  # Example: Times New Roman font, 10pt size

                # Apply the font to the label
                self.ui.label_working_path.setFont(font)
                self.ui.label_working_path.setText(f"<b><div align='center'>Workspace:<br><i>{WorkspaceName}</i></div></b>")  # Update the label text with the selected folder
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

    # Function to upload to the xml_tree
    def upload_xml_to_tree_widget(self, selected_file):
        if selected_file:
            # Clear existing items in the tree widget
            self.ui.treeWidget.clear()
            self.ui.treeWidget.setMaximumWidth(500)
            self.ui.treeWidget.setColumnWidth(0, 250)  # Set the width of the first column to 200 pixels
            self.ui.treeWidget.setColumnWidth(1,250)  # Adjust as necessary for your content

            try:
                # Parse the XML file
                tree = ET.parse(selected_file)
                root = tree.getroot()
                
                # Set the column count of the tree widget
                self.ui.treeWidget.setColumnCount(2)
                file_path = selected_file.split("/")
                for file_dir in file_path:
                    if ".xml" in file_dir:
                        filename = file_dir
                    else:
                        filename = file_path[len(file_path)-1]
                #self.ui.treeWidget.setHeaderHidden(True)
                self.ui.treeWidget.setHeaderLabels(["File", filename])

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
                        xmlElement = selected_item.data(0, Qt.UserRole)  # Retrieve the associated XML element
                        new_element_name, ok = QInputDialog.getText(self, "Add Child Element", "Enter the name of the new element:")
                        
                        if ok and new_element_name:
                            new_element = ET.SubElement(xmlElement, new_element_name)  # Create and append the new element
                            new_element_text, ok = QInputDialog.getText(self, "Set Value", "Enter the value for the new element:") ##No es necesario agregar el valor al elemento
                            
                            if ok:
                                new_element.text = new_element_text  # Set text for the new element
                                # Reflect the changes in the QTreeWidget
                                new_item = QTreeWidgetItem([new_element.tag])
                                selected_item.addChild(new_item)
                                
                                if new_element.text:
                                    value_item = QTreeWidgetItem(["Value", new_element.text])
                                    new_item.addChild(value_item)
                                
                                # Update the association for the new QTreeWidgetItem
                                new_item.setData(0, Qt.UserRole, new_element)
                                
                                # Write changes to the file
                                tree.write(selected_file, encoding="utf-8", xml_declaration=True)

                


                def add_attribute():
                    selected_item = self.ui.treeWidget.currentItem()
                    if selected_item is not None:
                        xmlElement = selected_item.data(0, Qt.UserRole)  # Retrieve the associated XML element
                        
                        if xmlElement is not None:
                            attribute_name, ok = QInputDialog.getText(self, "Add Attribute", "Enter the name of the new attribute:")
                            if ok and attribute_name:
                                attribute_value, ok = QInputDialog.getText(self, "Set Attribute Value", "Enter the value for the new attribute:")
                                if ok:
                                    xmlElement.set(attribute_name, attribute_value)  # Set attribute for the element
                                    
                                    # Update the QTreeWidgetItem display
                                    newAttr = QTreeWidgetItem([f"@{attribute_name}",attribute_value])
                                    selected_item.addChild(newAttr)

                                    
                                    # Optionally: Write changes back to XML file
                                    tree.write(selected_file, encoding='utf-8', xml_declaration=True)

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
                        tree.write(selected_file, encoding='utf-8', xml_declaration=True)

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
                    tree.write(selected_file, encoding="utf-8", xml_declaration=True)
                    
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

                    tree.write(selected_file, encoding="utf-8", xml_declaration=True)

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
                                    tree.write(selected_file, encoding='utf-8', xml_declaration=True)

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

                    
            

                
                # Enable context menu and connect signal
                self.ui.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
                self.ui.treeWidget.customContextMenuRequested.connect(openMenu)
                
                
                

                QMessageBox.information(self, "Success", "XML data loaded successfully into the tree widget.")

            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to parse XML file: {str(e)}")

        self.ui.TestActionsFrame.setMaximumWidth(350)

    #Función para enviar tests a la Raspberry y añadirlos a la cola
                
    def add_tests_to_queue(self):
        
        if self.ssh_link.connected:
            if self.currentPathToWorkspace != "":
                new_file_command = ["cd /Desktop","touch queued_tests.txt"]
                
            else:
                QMessageBox.warning(self, "Warning", f"No workspace has been selected, please choose a workspace to save the tests results")
        else:
            QMessageBox.warning(self, "Warning", f"An ssh connection must be established first, please select a device and the send the test")

    #Función para enviar tests

                
    #Función para establecer conexión con la rasp
    def ssh_connect(self):
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
                        if Exception:
                            QMessageBox.warning(self, "Warning", status)
                        self.ui.label_current_status.setPixmap(QPixmap(u":/icons/icons/zap.svg"))
                    else: 
                        QMessageBox.warning(self, "Warning", f"Password required")
                else:
                    ssh_dir = os.path.expanduser('~/.ssh') # Default private key location
                    private_key_path = os.path.join(ssh_dir, f'id_rsa')
                    public_key_path = f'{private_key_path}.pub'

                    # Check if both the private and public keys exist
                    private_key_exists = os.path.isfile(private_key_path)
                    public_key_exists = os.path.isfile(public_key_path)

                    if private_key_exists and public_key_exists:
                        status = self.ssh_link.connect(private_key_path)
                        if Exception:
                            QMessageBox.warning(self, "Warning", status)
                    else:
                        rpi_username, ok_username = QInputDialog.getText(self, "SSH Login", "Please enter path to your ssh private key directory:")
                        
                
            """
        if ok_hostname and rpi_hostname:
            rpi_username, ok_username = QInputDialog.getText(self, "SSH Login", "Please enter your username:")
            if ok_username and rpi_username:
                rpi_password, ok_password = QInputDialog.getText(self, "SSH Login", "Please enter your password:", QLineEdit.Password)
                if ok_password and rpi_password:
                    self.ssh_link = ssh(rpi_hostname,rpi_username,rpi_password)
                    QMessageBox.information(self, "Information", f"Connection established with {rpi_username}")
                    self.ui.label_current_status.setPixmap(QPixmap(u":/icons/icons/zap.svg"))
                else: 
                    QMessageBox.warning(self, "Warning", f"Password required")
            else:
                QMessageBox.warning(self, "Warning", f"Username required")
        else:
            QMessageBox.warning(self, "Warning", f"Hostname required to establish ssh connection")
        """        

    #Función para cerrar conexión ssh
    def ssh_close_connection(self):
        if self.ssh_link.connected:
            self.ssh_link.close_connection()
            QMessageBox.information(self, "Information", f"Connection closed with {self.ssh_link.hostname}")
            self.ui.label_current_status.setPixmap(QPixmap(u":/icons/icons/zap-off.svg"))
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

