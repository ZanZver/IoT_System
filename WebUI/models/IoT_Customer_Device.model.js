const mongoose = require("mongoose");

var devicesSchema = new mongoose.Schema({
    Smart_light:{},
    Smart_fridge:{},
    Smart_vacuum:{}
});

var IoT_Customer_Device = new mongoose.Schema({
    UserID: {
        type: String
    },
    Devices:{
        type: devicesSchema
    }
});

mongoose.model("IoT_Customer_Device", IoT_Customer_Device);