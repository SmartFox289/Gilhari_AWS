# gilhariaws
 
## Softwares used 

1. Docker Desktop: (version 26.1.1) for running Gilhari container
2. Postman: (v11.2.12) for testing Gilhari REST APIs on local database 
3. MySQL: (version 8) for creating and using database
4. Gilhari SDK: for source codes and configuration guide
5. JDBC driver for MySQL: for establishing connection to MySQL database

## Setup and configuration of Gilhari
After installing **Gilhari SDK** from [here](https://www.softwaretree.com/v1/products/gilhari/download-gilhari.php) follow these steps to configure Gilhari microservice.

### 1. Define and compile empty Java (container) class  
In `src\com\softwaretree\jdxjsonexample\model` create a file `JSON_Employee.java`. Here, Employee is a conceptual name for a type of JSON object. For defining any new container class `X`, you just have to create an `X.java` file and change `JSON_Employee` to `X` at three places in the code.

Create a `lib` directory and add `jdxtools.jar`, `json-20160212.jar` and `jxclasses.jar` which can be found in the `libs\` directory of Gilhari SDK  

Compile the classes using javac for JDX ORM to use them. Command for compiling:
```cmd
javac -source 8 -target 8 -cp "lib/jxclasses.jar;lib/jdxtools.jar;lib/json-20160212.jar" -d bin src/com/softwaretree/jdxjsonexample/model/JSON_Employee.java
```    
>Note: Use Java 8 or below for compiling, else it will create bytecode which will not be compatible with Gilhari. You can use later versions of Java elsewhere.

### 2. Define a Object Relational Mapping (ORM) specification
In `config` directory create a `.jdx` file and define the ORM specification.  

Also, in this directory add the database's JDBC driver as a `.jar`.  

> Gilhari framework ships three commonly used JDBC drivers in the directory `/node/node_modules/jdxnode/external_libs`  
But it is recommended to download and use the latest JDBC driver for your database, as the one provided may give errors while connecting to the database.

Add a file `.js` file in `config` to map "Employees" to the defined Employee container class. Repeat this for all the classes.

Finally, create a `.config` file and fill in the required fields.

### 3. Create a Dockerfile, build and run Docker container  
Create a Dockerfile as shown and run the following command to build the docker image:  
```cmd
docker build -t my_app_gilhari -f ./Dockerfile .
```

Run the docker image using the following command: 
```cmd
docker run -p 80:8081 my_app_gilhari
```

### If there were no errors, you have configured Gilhari successfully!
### Gilhari is now running on your localhost and you can make API calls through Postman.

>You an refer the Gilhari documentation for more information on the configuration process and the `.config` file and its fields.


## Creating Python virtual environment 
It's always a good idea to work on a virtual environment as it isolates the work from the local machine.  
To create a virtual environment named `newvenv` use the following command in your terminal: 
```cmd
python -m venv newvenv
```

Once you have created a virtual environment, activate it by running this command:   

For windows:
```cmd
newvenv\Scripts\activate
```

For Unix or MacOS: 
```cmd
source newvenv/bin/activate
```

Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using.

To deactivate the virtual environment use the following command:   
```cmd
deactivate
```

### You may face this error while activating your virtual environment:
>Running scripts is disabled on this system

This error occurs because the execution policy may be set to `Undefined` or `Restricted` which does not allow scripts to run.

To see the execution policy, open `windows powershell` and use the following command:
```cmd
Get-ExecutionPolicy
```

Set the execution policy to `RemoteSigned` 
```cmd
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

> You would have to run powershell as administrator for changing policy for localmachine scope

Click [here](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4) to learn more about execution policies.

