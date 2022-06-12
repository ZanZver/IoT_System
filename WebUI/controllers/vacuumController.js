//.lean()
const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const User = mongoose.model('User');
const Employee = mongoose.model('Employee');
const IoT_Customer_Device = mongoose.model("IoT_Customer_Device");

function updateRecord(req, res) {
    var userKeyID = "6280e95696737775cbc590d7";
    console.log(req.body);
    IoT_Customer_Device.findOneAndUpdate(
        { UserID: userKeyID }, 
        [{$set:req.body}], 
        { new: true }, 
        (err, doc) => {
        if (!err) { res.redirect('/devices/smart_vacuum'); }
        (err, doc) => {
            if (!err) { res.redirect('/devices/smart_vacuum'); }
            else {
                if (err.name == 'ValidationError') {
                    handleValidationError(err, req.body);
                    res.render("devices/edit_smart_vacuum", {
                        viewTitle: "Update smart vacuum",
                        device_smart_vacuum: data.smart_vacuum[req.body.Device_ID]
                    });
                }
                else
                    console.log('Error during record update : ' + err);
            }
        }
    }).lean();
}

router.post('/', (req, res) => {
    if (req.body._id == ''){
        console.log("Naah");
    }    
    else{
        updateRecord(req, res);   
    }
        
});

router.get('/', (req, res) => {
    let userKeyID =  "6280e95696737775cbc590d7";
    IoT_Customer_Device.aggregate([
        {$match: {UserID:userKeyID}},
        {$project: {
            _id:0,UserID:0
        }}
    ]).exec((err, docs) => {
        res.render("devices/smart_vacuum", {
            list: docs[0].smart_vacuum
        });
    });
});

router.get('/edit/:id', (req, res) => {
    itemId = req.params.id;
    userKeyID = "6280e95696737775cbc590d7";
    IoT_Customer_Device.findOne(
        {UserID: userKeyID},
        {"_id":0}
        ).lean().exec(function (err, data) {
            if (!err) {
                console.log(data.smart_vacuum[itemId]);
                res.render("devices/edit_smart_vacuum", {
                    viewTitle: "Update smart vacuum",
                    device_smart_vacuum: data.smart_vacuum[itemId]
                });
            }
            else { console.log('Error in device edit :' + err); };
        }
        );
});

router.get('/delete/:id', (req, res) => {
    let userKeyID =  "6280e95696737775cbc590d7";
    let removeLoc = "smart_vacuum.";
    removeLoc += req.params.id;
    
    IoT_Customer_Device.updateOne(
        { UserID: userKeyID },
        [{ $unset: removeLoc }],
        (err, data) => {
            if (!err) {
                res.redirect('/devices/smart_vacuum');
            }
            else { console.log('Error in device delete :' + err); }
        }
    );
});

module.exports = router;