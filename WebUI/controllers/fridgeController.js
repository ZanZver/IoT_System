//.lean()
const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const User = mongoose.model('User');
const Employee = mongoose.model('Employee');
const IoT_Customer_Device = mongoose.model("IoT_Customer_Device");

function updateRecord(req, res) {
    var userKeyID = "6280e95696737775cbc590d7";
    IoT_Customer_Device.findOneAndUpdate(
        { UserID: userKeyID }, 
        [{$set:req.body}], 
        { new: true }, 
        (err, doc) => {
        if (!err) { res.redirect('/devices/smart_fridge'); }
        (err, doc) => {
            if (!err) { res.redirect('/devices/smart_fridge'); }
            else {
                if (err.name == 'ValidationError') {
                    handleValidationError(err, req.body);
                    res.render("devices/edit_smart_fridge", {
                        viewTitle: "Update smart fridge",
                        device_smart_fridge: data.smart_fridge[req.body.Device_ID]
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
        res.render("devices/smart_fridge", {
            list: docs[0].smart_fridge
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
                console.log(data.smart_fridge[itemId]);
                res.render("devices/edit_smart_fridge", {
                    viewTitle: "Update smart fridge",
                    device_smart_fridge: data.smart_fridge[itemId]
                });
            }
            else { console.log('Error in device edit :' + err); };
        }
        );
});

router.get('/delete/:id', (req, res) => {
    let userKeyID =  "6280e95696737775cbc590d7";
    let removeLoc = "smart_fridge.";
    removeLoc += req.params.id;

    IoT_Customer_Device.updateOne(
        { UserID: userKeyID },
        [{ $unset: removeLoc }],
        (err, data) => {
            if (!err) {
                res.redirect('/devices/smart_fridge');
            }
            else { console.log('Error in device delete :' + err); }
        }
    );
});
module.exports = router;