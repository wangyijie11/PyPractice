var page = require('webpage').create();

console.log('the default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'SpecialAgent';
page.open('http://www.httpuseragent.org', function(status){
    if (status !== 'success'){
        console.log('unbale to access network');
    } else {
        <!--有问题-->
        var ua = page.evaluate(function() {
            return document.getElementById('myagent').textContent;
        });
        console.log(ua);
    }
    phantom.exit();
});
