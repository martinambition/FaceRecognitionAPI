# In-Store Analytics

Click-throughs, bounce rates, segmentation and conversion funnels are common and essential metrics for any online store. Brands which do not employ these to enhance the experience will miss out on targeted content, display optimization and personalized recommendations which account for over 20% of an online-stores revenue.

When it comes to bricks and mortar these tools are sorely missing. Sessions, cookies and preferences just don't exist in the real world until now.

We take the latest artificial intelligence breakthroughs in the field of vision-based Human Computer Interaction (HCI) to change the game. With In-Store Analytics, B1 Retailers can leverage the power of digital footprints to apply the same tools as their online counterpart


<img src="https://raw.githubusercontent.com/martinambition/FaceRecognitionAPI/master/inshop.jpg" width="100%">

![image](https://raw.githubusercontent.com/martinambition/FaceRecognitionAPI/master/report1.png)

![image](https://raw.githubusercontent.com/martinambition/FaceRecognitionAPI/master/report2.png)



## Installation
You could choose to install from release build or complie the source code by yourself. Currently, we only support windows platform. MacOS & Linux will being supported soon.

---
### Install from release build (Recommand):
#### Requirements
  * Java Runtime Environment
  * [SQL Server](https://www.microsoft.com/en-us/download/details.aspx?id=1695/)
#### Installation Guidance
1. Download release [build](http://note.youdao.com/)
2. Unzip build.zip
3. Setup the database
    1. Create a database named "**ShopAnalytics**"
    2. Execute "DB/**DBCreate.sql**"

#### How to Run
1. Go to the unzipped folder
2. Run "InitData.bat" and input the account & password of database
3. Run "CameraServer.exe" 
4. Run "AnalyticsServer.bat" and input the account & password of database
5. Open "http://localhost:8080/client/index.html"

----

### Install from source code on Windows:

#### Requirements

  * [SQL Server](https://www.microsoft.com/en-us/download/details.aspx?id=1695/)
  * [Anaconda](https://www.anaconda.com/download/) 
  * JDK 1.8
  * [Gradle](https://gradle.org/install/#manually)

#### Installation Guidance

In-Store Analytics contains three parts (Database, Camera Server and Analytics Server).

1. Clone/Dowload source code from repo
2. Setup the database
    1. Create a database named "**ShopAnalytics**" 
    2. Execute "DB/**DBCreate.sql**"
3. Install Camera Server(python)
    1. Open your Anaconda Prompt from the start menu
    2. Change directory to the Camera folder
    3. Run below command 
    ```console
        conda env create -f environment.yml -n face
    ```
4. Install Analytics Server(java)
    1. Change directory to Analytics folder
    2. Fill the connection string of db in application.properties 
    2. Run below command to build java source code.
    ```console
        gralde build
    ```

#### How to Run
1. Run "InitData.bat" and input the account & password of database
1. Run below command to start the python server
    ```console
        python server.py
    ```
2. Run below command. please change the username and password accordingly
    ```console
        java -jar ServerCenter-0.0.1.jar --spring.datasource.username=sa --spring.datasource.password=XX
    ```
3. Open "http://localhost:8080/client/index.html"

## License
In-Store Analytics is released under the terms of the MIT license. See LICENSE for more information or see https://opensource.org/licenses/MIT.
