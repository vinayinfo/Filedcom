# Filedcom web app design

Clone project from github
- `git clone git@github.com:vinayinfo/Filedcom.git`
- `cd Filedcom`
- `docker-compose up web`
          
# challenge Description

Write a Flask / FastAPI Web API that simulates the behavior of an audio file server
while using a MongoDB / SQL database.

Requirements: You have one of three audio files which structures are defined below
Audio file type can be one of the following:

    1 – Song
    2 – Podcast
    3 – Audiobook
    
##`Song` file fields:
- `ID` – (mandatory, integer, unique)
- `Name of the song` – (mandatory, string, cannot be larger than 100
characters)
- `Duration in number of seconds` – (mandatory, integer, positive)
- `Uploaded time` – (mandatory, Datetime, cannot be in the past)


## `Podcast` file fields:
- `ID` – (mandatory, integer, unique)
- `Name of the podcast` – (mandatory, string, cannot be larger than 100
characters)
- `Duration in number of seconds` – (mandatory, integer, positive)
- `Uploaded time` – (mandatory, Datetime, cannot be in the past)
- `Host` – (mandatory, string, cannot be larger than 100 characters)
- `Participants` – (optional, list of strings, each string cannot be larger than
100 characters, maximum of 10 participants possible)


##`Audiobook` file fields:
- `ID` – (mandatory, integer, unique)
- `Title of the audiobook` – (mandatory, string, cannot be larger than 100
characters)
- `Author of the title` (mandatory, string, cannot be larger than 100
characters)
- `Narrator` - (mandatory, string, cannot be larger than 100 characters)
- `Duration in number of seconds` – (mandatory, integer, positive)
- `Uploaded time` – (mandatory, Datetime, cannot be in the past)



API structuture is define in documentation folder. it is postman structure

Test challenge summary is define in documentation folder


# How to TEST APIS
Test api structure is given in documentation, it is postman exported one.

# apis end point

#### 1. create
    url = /api/create/ 
    method = Post
    content-type=application/json
    
   - structures:
        - song 
                
             request body
                
               {
                "audioFileType":"song",
                "audioFileMetadata":{
                    "uploaded_time":<upload time>>,
                    "duration_time":<time duration in seconds>,
                    "name":"<name of song>"
                    }
                }
        - podcast
            
            - request body
                   
                   {
                        "audioFileType":"podcast",
                        "audioFileMetadata":{
                                "uploaded_time":"0",
                                "duration_time":102,
                                "name":"in the end.mp4",
                                "host":"linkin park - arizona park",
                                "participents":["linkin park","us","american band"]
                        }
                     }      
        - audiobook
        
            - request body
            
                    {
                        "audioFileType":"audiobook",
                        "audioFileMetadata":{
                                "uploaded_time":"0",
                                "duration_time":102,
                                "title":"in the end.mp4",
                                "author":"linkin park",
                                "narrator":"linkin park"
                        }
                    }
                    
####2. Update

    url = /api/<audioFileType>/<audioFileID>/ 
    method = PUT
    content-type=application/json
- song
    
    - url : `/api/song/1/`
    - request body :
            
            {
                "audioFileType":"song",
                "audioFileMetadata":{
                        "uploaded_time":"0",
                        "duration_time":102,
                        "name":"in the end - metoria by linkin park.mp4"    
                }
            }
        
        
    
- podcast
    
    - url : `/api/podcast/1/`
    - request body : 
    
            {
                "audioFileType":"podcast",
                "audioFileMetadata":{
                    "uploaded_time":"0",
                    "duration_time":102,
                    "name":"linkin park in the end.mp4",
                    "host":"linkin park - arizona park",
                    "participents":["linkin park","us","american band"]    
                 }    
        }
    
    
- audiobook
    
    - url : `/api/audiobook/1/`       
    - request body:
    
            {
            "audioFileType":"audiobook",
            "audioFileMetadata":{
                    "uploaded_time":"0",
                    "duration_time":102,
                    "title":"in the end.mp4",
                    "author":"linkin park- mike shindoda",
                    "narrator":"linkin park"  
            }
        }

##3. delete
  
    url = /api/<audioFileType>/<audioFileID>/
    method = DELETE
    content-type = application/json
    
- song
    - url: `/api/song/1` - delete record present at id 1
- podcast
    - url: `/api/podcast/1` - delete record present at id 1
- audiobook
    - url : `/api/audiobook/1` - delete record present at id 1

##4. get

   1. - url:  `/api/<audioFileType>`
      - description: `get all the data present in <audioFileType> database`
   2.- url:  `/api/<audioFileType>/<audioFileID>`
      - description: `get all data present in <audioFileType> database having id `audioFileID`    
   3. ###### urls
   
        1. song,
           
               url1 = `/api/song/` - get all song in database
               url2 = `/api/song/1/` - get song having id 1       
               
        2. podcast
           
               url1 = `/api/podcast/` - get all data in podcast in database
               url2 = `/api/podcast/1/` - get song having id 1
           
         3. audiobook
           
          url1 = `/api/audiobook/` - get all data in audiobook in database
          url2 = `/api/audiobook/1/` - get data having id 1
    
    
### Return from REQUEST

    - Action is successful: 200 OK
    - The request is invalid: 400 bad request
    - Any error: 500 internal server error