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

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_IPTC()
        self.ui.setupUi(self)
        self.currentPathToWorkspace = ""
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
        ## Stacked Widget for New/Saved organization
        ## Establecer página de inicio por defecto
        self.ui.stackedWidgetWorkspace.setCurrentWidget(self.ui.home)

        #Cambiar a la página designada para espacio de trabajo guardado
        self.ui.selectWorkspaceBtn.clicked.connect(self.select_workspace_and_change_widget)

        #Añadir file al treewidget
        self.ui.tests_recent_btn.clicked.connect(self.upload_xml_to_tree_widget)


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
        self.ui.devBtnTest.clicked.connect(lambda: self.slideDownMenu(self.ui.slide_devtstmenu,self.ui.devBtnTest))
        self.ui.devBtnTest.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt))

        #Configure workspace toggle button
        self.ui.confWorkspaceBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.confWokspace_menu,self.ui.confWorkspaceBtn))
        self.ui.confWorkspaceBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt))

        #Data results toggle button
        self.ui.dataResultBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.dataResults_menu,self.ui.dataResultBtn))
        self.ui.dataResultBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt))        

        #Help toggle button
        self.ui.helpBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.help_menu,self.ui.helpBtn))
        self.ui.helpBtn.clicked.connect(lambda: self.ui.stackedDataResults.setCurrentWidget(self.ui.homeDataResOpt))   
        #Data results side menu toggle button
        self.ui.sideResultsBtn.clicked.connect(lambda: self.slideLeftMenu(self.ui.dataresult_sidemenu,self.ui.sideResultsBtn))

        #Develop and run tests side menu toggle button
        self.ui.side_btn_tests.clicked.connect(lambda: self.slideLeftMenu(self.ui.testsopt_slide,self.ui.side_btn_tests))


        #Develop and run tests side menu toggle button
        self.ui.newSeqBtn.clicked.connect(lambda: self.slideLeftMenu(self.ui.newSeq_slidemenu,self.ui.newSeqBtn))

        #Add members edit line
        self.ui.addMembersBtn.clicked.connect(lambda: self.slideDownMenu(self.ui.addMembersLine,self.ui.addMembersBtn))
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
    def slideDownMenu(self,slidedown_menu,btn):
        # Obtener ancho de la ventana de menu
        height = slidedown_menu.height()
        # Si está minimizado
        menus = ["Develop and run tests","Configure Workspace","Data results","Help"]
        if btn.text() in menus:
            menus.remove(btn.text())
            if height == 0:
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

                    if frame.height() > 0:
                        frame.setMaximumHeight(0)
                        actBtn.setIcon(QtGui.QIcon(actBtnIconPath))

                # Expandir Menú
                newHeight = 800
            
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
                newHeight = 800

            else:
                newHeight = 0

        # Transición animada
        self.animation = QPropertyAnimation(slidedown_menu, b"maximumHeight")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(height)#Start value is the current menu width
        self.animation.setEndValue(newHeight)#end value is the new menu width
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
            self.ui.label_working_path.setText(name)  # Update the label text
            with open(f"{pathToWorkspace}/Workspace_Info.txt", "w") as file:
                file.write(f"Name: {name}\n")
                file.write(f"Organization: {org}\n")
                file.write(f"Team: {team}\n")
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

    # Function to select a saved workspace
    def select_workspace(self):
        options = QFileDialog.Options()
        selected_folder = QFileDialog.getExistingDirectory(self, "Select Workspace", options=options)

        if selected_folder:
            # Check if the selected folder contains the .iptc file
            iptc_file_path = os.path.join(selected_folder, ".iptc")
            if os.path.exists(iptc_file_path):
                self.currentPathToWorkspace = selected_folder
                self.ui.label_working_path.setText(selected_folder)  # Update the label text with the selected folder
                QMessageBox.information(self, "Information", "Workspace selected successfully")
            else:
                QMessageBox.warning(self, "Warning", "Selected folder is not a valid workspace")

    # Function to upload to the xml_tree
    def upload_xml_to_tree_widget(self):
        options = QFileDialog.Options()
        selected_file, _ = QFileDialog.getOpenFileName(self, "Select XML File", "", "XML Files (*.xml)", options=options)

        if selected_file:
            # Clear existing items in the tree widget
            self.ui.treeWidget.clear()

            try:
                # Parse the XML file
                tree = ET.parse(selected_file)
                root = tree.getroot()

                # Add root item to the tree widget
                root_item = QTreeWidgetItem(self.ui.treeWidget)
                root_item.setText(0, root.tag)

                # Recursive function to add child items
                def add_items(parent_item, xml_element):
                    for child in xml_element:
                        child_item = QTreeWidgetItem(parent_item)
                        child_item.setText(0, child.tag)
                        child_item.setExpanded(True)
                        add_items(child_item, child)

                # Populate the tree widget with XML data
                add_items(root_item, root)

                QMessageBox.information(self, "Success", "XML data loaded successfully into the tree widget.")

            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to parse XML file: {str(e)}")


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

