//.lean()
const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const User = mongoose.model('User');
const Employee = mongoose.model('Employee');
const IoT_Customer_Device = mongoose.model("IoT_Customer_Device");

router.get('/', (req, res) => {
    let userKeyID =  "6276a2a8e59469e642802063";
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

router.get('/delete/:id', (req, res) => {
    let userKeyID =  "6276a2a8e59469e642802063";
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