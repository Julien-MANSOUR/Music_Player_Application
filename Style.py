def groupBoxStyle():#usualy we use the of the class(here QGroupbox) and inside it the style
    return """
            QGroupBox{
            background-color:aqua;
            font:15pt Times Bold;
            color:black;
            border:2xp solid gray;
            border-radius:15px;
  }
    """

def progressBarStyle():
    return '''
            QProgressBar{
            border:1px solid #000000;
            background:white;
            height: 10px;
            border-radius: 6px;
         
            
            }
    
    '''

def playListStyle():
    return """
            QListWidget{
            background-color:#fff;
            border-radius: 10px;
            border: 3px solid aqua;
    
    
    
    }
    
    
    
    """