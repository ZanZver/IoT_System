const mongoose = require("mongoose");

mongoose.connect('mongodb://localhost:27019,localhost:27020,localhost:27021/initialDB', {useNewUrlParser: true}, (err) => {
    if(!err){
        console.log("MongoDB Conncetion Succeeded!")
    }
    else{
        console.log("Error in DB connection: " + err)
    }
});

require("./employee.model");
require("./user.model.js");
require("./IoT_Customer_Device.model.js");
require("./IoT_Device_Info.model.js");