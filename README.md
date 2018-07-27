# PyAutoman
See [AutoMan](https://automan-lang.github.io/)
This package is currently in development.

### System Requirements
To use this package you must be running Python 2.7.15 or 3.2+, and Scala 2.11.7+. This package relies on [ScalaPB](https://scalapb.github.io/) and [gRPC](https://grpc.io/). If you use SBT to build this project, all Scala dependencies will be downloaded. To install gRPC for Python (needed for the Python client), follow these [instructions](https://grpc.io/docs/quickstart/python.html).


### How to Build 
The easiest way to build this project is by using [SBT](https://www.scala-sbt.org/). To build this project, from the /PyAutoman directory, run
```
sbt clean compile pack
```
SBT will also compile the necessary .proto into Scala classes automatically. To generate the the python files needed, `grpcio-tools` and `googleapis-common-protos` need to be installed. These python dependencies are automatically installed by pip if this package is installed from the provided tarball (). To install the necessary packages manually, run the following two commands:
```
pip install grpcio-tools
pip install googleapis-common-protos
```
To use gRPC generate the python files needed for interacting with the RPC service, from the /PyAutoman directory, run the following command:

```
python -m grpc_tools.protoc -I src/main/protobuf/ --python_out=src/main/pyautoman/pyautoman/core/grpc_gen_classes --grpc_python_out=src/main/pyautoman/pyautoman/core/grpc_gen_classes src/main/protobuf/automanlib_rpc.proto src/main/protobuf/automanlib_classes.proto src/main/protobuf/automanlib_wrappers.proto
```

Move the files compiled by sbt into the correct directory by copying them:
```
cp -r target/pack/ src/main/pyautoman/pyautoman/core/rpc/server/
```

Then change to the directory containing setup.py and run it from there:
```
cd src/main/pyautoman/
python setup.py sdist
```
Alternaltively, you can run `./buildproject.sh` located in the root directory, the do the steps outlined above.

### How to Install
To install this package without building, use pip install to install the tarball in the directory PyAutoMan/src/main/pyautoman/dist/ 
```
pip install pyautoman-0.1.0.dev0.tar.gz
```

### How to Use
To run tasks, first create an Automan object. Automan objects require an adapter, and take optional parameters for the RPC server address and port number (default is 'localhost' and 50051).  The adapter we pass to the constructor is simply a dictionary with the following required fields:
* access_id - the login id for the crowdsource backend
* access_key - the login access key for the crowdsource backend
* type - the type of crowdsource backend. currently only "mturk" is an accepted type

First, import the Automan and EstimateOutcome classes from pyautoman.automan, then create an adapter

```python
Python 2.7.15 |Anaconda, Inc.| (default, May  1 2018, 18:37:05) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
from pyautoman.automan import Automan, EstimateOutcome
>>> adapter = {
...     "access_id" : "access id here",
...     "access_key" : "access key here",
...     "sandbox_mode" : "true",
...     "type" : "MTurk"
... }

```

When the creating Automan object is being initialized, if the server_addr is 'localhost' it will start a local AutoMan RPC server as a new process, configured to listen on the provided port number. Future functionality will allow users to connect to remote RPC servers. We can now use the Automan object to submit tasks to the crowdsource back-end. Currently, only the `estimate` function of Automan is available. See example code for usage.

```python
>>> a = Automan(adapter, server_addr='localhost',port=50051)
python client is starting server...
Server Started on port 50051 ...
>>> photo_url = "https://docs.google.com/uc?id=1ZQ-oL8qFt2tx_T_-thev2O4dsugVbKI2"
>>> estim = a.estimate(text = "How full is this parking lot?",budget = 1.00, title = "Car Counting",image_url = photo_url)
```

Each type of task has fields that are required. All tasks require `text` (a text description of the task), `image_url` and `budget` (desired upper limit of cost of task). We specify the tasks we would like AutoMan to carry out, and either when the question has timed out and budget is exceeded (resulting in a low confidence or overbudget outcome respectively) or the desired confidence level has been met. If the task went overbudget, the need and have fields of the returned EstimateOutcome are initialized, otherwise high, low, est, cost, and conf are initialized. Autman returns gRPC's implementation of Futures. To ensure the future is resolved before values are accessed, only try to access respective values within code blocks that ensure those values are set. See methods `isConfident()`, `isLowConfidence()`, and `isOverBudget()` below.


To simply print the result of the task, use `printOutcome()`.
```python
estim.printOutcome()
>>> estim.printOutcome()
Outcome: Low Confidence Estimate
Estimate low: 62.000000 high:62.000000 est:62.000000
```

The outcome can be either:
*Estimate
*Low Confidence estimate
*Overbudget



### Example Code 
```python
from pyautoman.automan import Automan, EstimateOutcome

# make mechanical turk adapter
adapter = {
	"access_id" : "access id here",
    "access_key" : "access key here",
    "sandbox_mode" : "true",
    "type" : "MTurk"
}




# image to submit with our task
photo_url = "https://docs.google.com/uc?id=1ZQ-oL8qFt2tx_T_-thev2O4dsugVbKI2"

# make AutoMan object 
# 'suppress_output' sets the level of output for RPC server to stdout. current valid values are
# 	"all" 	- suppress all output
# 	"none "	- show all output 
a = Automan(adapter, server_addr='localhost',port=50051,suppress_output="none")

estim = a.estimate(text = "How many cars are in this parking lot?",
    budget = 6.00,
    title = "Car Counting",
    confidence_int = 10,
    image_url = photo_url)

if(estim.isConfident()):
	print("Outcome: Estimate")
	print("Estimate low: %f high:%f est:%f "%(estim.low, estim.high, estim.est))


if(estim.isLowConfidence()):
	print("Outcome: Low Confidence Estimate")
	print("Estimate low: %f high:%f est:%f "%(estim.low, estim.high, estim.est))

if(estim.isOverBudget()):
	print("Outcome: Over Budget")
	print(" need: %f have:%f"%(estim.need, estim.have))

# this is temporary, in future client will automatically handle shutdown
# to be safe, only call _shutdown() after the future has resolved,
# or else the server will kill itself before the computation is finished 
a._shutdown()
```
You can run the code on MTurk with the 'sandbox_mode' option set to 'true' and submit a response (need to create requester developer sandbox and worker sandbox accounts) to submit dummy worker responses. Here is what the output would look like if a single worker submitted a response of 62.
Output:
```python
Outcome: Low Confidence Estimate
Estimate low: 62.000000 high:62.000000 est:62.000000 
```
## API
### AutoMan Class 
#### **Constructor**
```python
Automan(self, adapter, server_addr = 'localhost', port = 50051, suppress_output = 'all')
```
**adapter** 		- the adapter credentials to use to connect to the crowdsource backend
**server_addr**		- the hostname address of the gRPC Automan server to connect to
**port** 			- the port number to connect to the gRPC Automan server
**supress_output**	- the level of output to show from the gRPC Automan server. "none" shows all output, "all" supresses all output from server

#### AutoMan Class Methods
```python
Automan.estimate(self, text, budget, image_url, title = "", confidence = 0.95, confidence_int = -1, img_alt_txt = "",  
sample_size = -1,dont_reject = True, pay_all_on_failure = True, dry_run = False, wage = 11.00,  
max_value = sys.float_info.max, min_value = sys.float_info.min, question_timeout_multiplier = 500,  
initial_worker_timeout_in_s = 30)
```
###### Description
	Provides AutoMan's estimate functionality. Uses the crowdsource backend to obtain a 
	quality-controlled estimate of a single real value. 
###### Return Type
	`EstimateOutcome`
###### Parameters
* **text** 							- the text description of the task to display to the worker 
* **budget** 						- the threshold cost for the task
* **image_url**  					- an image url to be associated with the task
* **title**   						- title of the task, displayed to worker
* **confidence** 					- desired confidence leve
* **confidence_int** 				- desired confidence interval
* **img_alt_txt** 					- alternative image text, for generated webpage displayed to worker
* **sample_size** 					- desired sample size, default of -1 indicates to use default samp. size of 30
* **dont_reject** 					- indicate whether to accept all answers automatically or not (?)
* **pay_all_on_failure** 			- indicate whether to pay all workers on task failure or note (?)
* **dry_run** 						- indicate whether to do a dry run or not
* **wage** 							- minimum wage to pay the worker, in USD/hr
* **max_value** 					- min value for dimension being estimated
* **min_value** 					- max value for dimension being estimated
* **question_timeout_multiplier** 	- timeout for the question on the crowdsource backend (default 500 mins?)
* **initial_worker_timeout_in_s** 	- timeout in seconds for the worker thread in the RPC server (defaul value )

### EstimateOutcome Class
Instances of this class will always be created for the user. This class will never need to be instantiated manually.  

#### EstimateOutcome Class Attributes
This class contains a Future, representing the outcome of the task. To ensure that the future is always resolved first
and the respective attributes are initialized, always use attributes of an EstimateOutcome in a code block that ensures
those values are set. Attributes are as follows:  
For `Confident` and `LowConfidence` outcomes:
* **high** 	- the highest value a worker reported
* **low** 	- the lowest value a worker reported
* **est** 	- AutoMan's estimate value
* **cost**	- the cost to complete the task
* **conf** 	- the confidence interval of the estimate  

For `OverBudget` outcomes:  
* **need** 	- the amount needed for AutoMan to continue attempting to obtain an estimate
* **have** 	- the current amount budgeted for the task  

#### EstimateOutcome Class Methods
##### EstimateOutcome.isConfident()
###### Description
		Indicates if the outcome of the task is a confident estimate
###### Return Type
		`boolean` : True if the outcome met the desired confidence level and interval, False otherwise
 
##### EstimateOutcome.isLowConfidence()
###### Description
		Indicates if the outcome of the task is a low confidence estimate
###### Return Type
		`boolean` : True if the outcome was a low confidence estimate, False otherwise
 
 
##### EstimateOutcome.isOverBudget()
###### Description
		Indicates if the outcome of the task is over budget or not
###### Return Type
		`boolean` : True if the outcome was over budget, False otherwise

