from krita import *

class QuickToggleHidden(Extension):

    visbleSet = None
    currentDepth = 0
    maxDepth = 32

    def __init__ (self,parent):
        super().__init__(parent)

    def setup(self) :
        print("QuickToggleHidden Setup")
        
    def toggleHide(self, colIndex:int) :
        nodes = Application.activeDocument().topLevelNodes()
        self.visbleSet = None
        self.currentDepth = 0
        self.toggleHideLoop(nodes, colIndex)
    
    def toggleHideLoop(self, nodes, colIndex) :
        for node in nodes:
            print(f'{node.name()} {node.colorLabel()}')
            if not node.locked():
                if node.colorLabel() == colIndex :
                    if self.visbleSet is None:
                        self.visbleSet = not node.visible()
                    node.setVisible(self.visbleSet)
                if node.childNodes() and (self.currentDepth < self.maxDepth):
                    self.toggleHideLoop(node.childNodes(), colIndex)
    
    def createActions(self,window):
        # enumerate later idk
        self.quicktogglehidden_blu = window.createAction("quicktogglehidden_blu", "Toggle Hide Blue", "")
        self.quicktogglehidden_gre = window.createAction("quicktogglehidden_gre", "Toggle Hide Green", "")
        self.quicktogglehidden_yel = window.createAction("quicktogglehidden_yel", "Toggle Hide Yellow", "")
        self.quicktogglehidden_orn = window.createAction("quicktogglehidden_orn", "Toggle Hide Orange", "")
        self.quicktogglehidden_brn = window.createAction("quicktogglehidden_brn", "Toggle Hide Brown", "")
        self.quicktogglehidden_red = window.createAction("quicktogglehidden_red", "Toggle Hide Red", "")
        self.quicktogglehidden_prp = window.createAction("quicktogglehidden_prp", "Toggle Hide Purple", "")
        self.quicktogglehidden_blk = window.createAction("quicktogglehidden_blk", "Toggle Hide Black", "")
    
        
        @self.quicktogglehidden_blu.triggered.connect
        def on_quicktogglehidden_blu_trigger():
            self.toggleHide(1)
            
        @self.quicktogglehidden_gre.triggered.connect
        def on_quicktogglehidden_gre_trigger():
            self.toggleHide(2)
        
        @self.quicktogglehidden_yel.triggered.connect
        def on_quicktogglehidden_yel_trigger():
            self.toggleHide(3)
        
        @self.quicktogglehidden_orn.triggered.connect
        def on_quicktogglehidden_orn_trigger():
            self.toggleHide(4)
        
        @self.quicktogglehidden_brn.triggered.connect
        def on_quicktogglehidden_brn_trigger():
            self.toggleHide(5)
        
        @self.quicktogglehidden_red.triggered.connect
        def on_quicktogglehidden_red_trigger():
            self.toggleHide(6)
        
        @self.quicktogglehidden_prp.triggered.connect
        def on_quicktogglehidden_prp_trigger():
            self.toggleHide(7)
        
        @self.quicktogglehidden_blk.triggered.connect
        def on_quicktogglehidden_blk_trigger():
            self.toggleHide(8)

Krita.instance().addExtension(QuickToggleHidden(Krita.instance()))