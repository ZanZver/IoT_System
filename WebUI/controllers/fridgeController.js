//.lean()
const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const User = mongoose.model('User');
const Employee = mongoose.model('Employee');
const IoT_Customer_Device = mongoose.model("IoT_Customer_Device");

router.get('/', (req, res) => {
    let userKeyID =  "627684d385abcb7f2331455d";
    IoT_Customer_Device.aggregate([
        {$match: {UserID:userKeyID}},
        {$unwind: "$Devices"
        },
        {$project: {
            "smart_fridge" : "$Devices.smart_fridge",
            "_id": 0
        }}
    ]).exec((err, docs) => {
        res.render("devices/smart_fridge", {
            list: docs[0].smart_fridge
        });
    });
});
module.exports = router;