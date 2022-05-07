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
            "smart_light" : "$Devices.smart_light",
            "_id": 0
        }}
    ]).exec((err, docs) => {
        res.render("devices/smart_light", {
            list: docs[0].smart_light
        });
    });
});

router.get('/delete/:id', (req, res) => {
    let userKeyID =  "627684d385abcb7f2331455d";
    console.log("hello");
    console.log(req.params.id);
    let toUnset = "Devices.smart_light.";
    toUnset += req.params.id;
    console.log(toUnset);

    var myquery = {UserID: "627684d385abcb7f2331455d"};
    var newvalues = {$unset:{"Devices":""}};

    //removes devices
    /*
    IoT_Customer_Device.findOneAndUpdate(
        {UserID: "627684d485abcb7f233145ab"}, 
        {$unset:{"Devices":1}},
        {new: true, overwrite: true},
        (err, res) =>
        {
        if (err) throw err;
        console.log(res);
    });
    */

    /*
    IoT_Customer_Device.remove(
        { "Devices.smart_light":1 },
        {UserID: "6275baf741e9a72a1eb7896f"}, 
        function(err, result) {
        if (err) {
          console.err(err);
        } else {
          res.json(result);
        }
    });
    */
    //IoT_Customer_Device.updateOne();

    /*
    IoT_Customer_Device.findOneAndUpdate(
        {UserID: "6275baf741e9a72a1eb7896f"}, 
        {$unset:{"Devices.smart_light":1}},
        {new: true, overwrite: true},
        (err, res) =>
        {
        if (err) throw err;
        console.log(res);
    });
    */
    /*
    IoT_Customer_Device.updateOne(myquery, newvalues, function(err, res) {
        if (err) throw err;
        console.log("1 document updated");
    });
    */


    /*
    IoT_Customer_Device.updateOne(
        {UserID: userKeyID}, 
        {"$unset":{"Devices.smart_light.0":""}}, 
        function (err, docs) {
        if (err){
            console.log(err)
        }
        else{
            console.log(docs);
        }
    });
    */
    /*
    IoT_Customer_Device.updateOne(
        {UserID: userKeyID}, 
        {"$unset":{toUnset:""}}, 
        function (err, docs) {
        if (err){
            console.log(err)
        }
        else{
            console.log(docs);
            res.redirect('/devices/smart_light');
        }
    });
    */
    res.redirect('/devices/smart_light');
    /*
    IoT_Customer_Device.updateOne({UserID: userKeyID}, 
        {"$unset":{"Devices.smart_light.0":""}}, 
        function (err, docs) {
        if (err){
            console.log(err)
        }
        else{
            res.redirect('/devices/smart_light');
        }
    });
    */
    //res.redirect('/devices/smart_light');
    /*
    IoT_Customer_Device.findByIdAndRemove(req.params.id, (err, doc) => {
        if (!err) {
            res.redirect('/delete/smart_light');
        }
        else { console.log('Error in employee delete :' + err); }
    }).lean();
    */
});
module.exports = router;