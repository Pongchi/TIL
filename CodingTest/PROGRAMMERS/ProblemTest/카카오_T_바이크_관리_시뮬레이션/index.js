const express = require('express');

const app = express();

app.use(express.json());
app.use(express.urlencoded({
    extended: true
}));

const X_AUTH_TOKEN = 'ae695a5930b902d6d316c24f7857abdc';
const AUTH_KEY = '1fd74321-d314-4885-b5ae-3e72126e75cc';
let Current_Time = -1

app.post('/start', (req, res) => {
    let TOKEN = req.get('X-Auth-Token');
    let Content_Type = req.get('Content-Type');

    if (Content_Type == 'application/json' && TOKEN == X_AUTH_TOKEN) {
        let problem = ParseInt(req.body.problem);
        if ( problem != NaN && 1 <= problem && problem <= 2) {
            Current_Time = 0;
            res.status(200).json({
                "auth_key" : AUTH_KEY,
                "problem" : problem,
                "time" : Current_Time
            });
        } else {
            return res.status(400).send('Parameter가 잘못됨 (범위, 값 등)');
        }
    } else {
        return res.status(401).send('인증을 위한 Header가 잘못됨');
    }
});

app.get('/locations', (req, res) => {
    let Key = req.get('Authorization');
    let Content_Type = req.get('Content-Type');

    if (Content_Type == 'application/json' && Key == AUTH_KEY) {
        return res.status(200).json({}); // 머임
    } else {
        return res.status(401).send('인증을 위한 Header가 잘못됨');
    }
});

app.listen(3000, () => {
    console.log("Running on Server");
})