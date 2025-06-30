terraform { 
  cloud { 
    
    organization = "joshuadlillie" 

    workspaces { 
      name = "twitter-bot-1" 
    } 
  } 
}