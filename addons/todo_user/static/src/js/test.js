odoo.define('todo_user', function(require) {
    "use strict";
    var core = require('web.core');
    var _t = core._t;
    var Session = require('web.Session');
    // var sess = require('web.session');
    // var Model = require('web.DataModel');
    // var QWeb = core.qweb;

    var url = "/hdwolf";
    var connection = new Session(undefined, url, {
        use_cors: true
    });

    for (var i = 0; i < 10; i++) {
        connection.rpc('', {}, {
                timeout: 7500
            })
            .then(function(barcode) {
                console.log(barcode);
            }, function() {
                console.log(arguments);
            });
    }
});


// I'm learning odoo web side developing. I wrote a very simple demo but met authority problem.

// I have a module `hdwolf` contains only one controller which simply returns a string:



// class HDWOLF(http.Controller):

//     @http.route('/hdwolf', type='json', auth='none', cors='*')

//     def saywolf(self):

//         return 'this is wolf'



// I can successfully query this domain `localhost:8069/hdwolf` using curl with a JSON header:

// `curl -i -X POST -H "Content-Type: application/json" -d "{}" localhost:8069/hdwolf`


// The problem emerges when I dev on web side. I want to query `localhost:8069/hdwolf` from another module, say "todo_user". It only contains an rpc query in `static/src/js`, nothing else:

// odoo.define('todo_user', function(require) {

//     "use strict";

//     var core = require('web.core');

//     var _t = core._t;

//     var sess = require('web.session');



//     var url = "/hdwolf";

//     var connection = new Session(undefined, url, {

//         use_cors: true

//     });



//     connection.proxy('/hdwolf', {}, {

//             timeout: 500

//         })

//         .then(function(barcode) {

//             alert(core._t('ajepoi'));

//         }, function() {

//             alert(core._t('something wrong'));

//         });

// });
