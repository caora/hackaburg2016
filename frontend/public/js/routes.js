module.exports = function(app, passport) {

// normal routes ===============================================================
//WICHTIG: http://stackoverflow.com/questions/12276046/nodejs-express-how-to-secure-a-url

    // show the home page (will also have our login links)
    app.get('/', function(req, res) {
        res.redirect('/home');
    });

      // LOGOUT ==============================
    app.get('/logout', function(req, res) {
        req.logout();
        res.redirect('/');
    });

// =============================================================================
// AUTHENTICATE (FIRST LOGIN) ==================================================
// =============================================================================

    // locally --------------------------------
        // LOGIN ===============================
        // show the login form
        app.get('/login', function(req, res) {
            res.render('login.ejs', { message: req.flash('loginMessage') });
        });

        // process the login form
        app.post('/login', passport.authenticate('local-login', {
            successRedirect : '/home', // redirect to the secure profile section
            failureRedirect : '/login' , // redirect back to the signup page if there is an error
            failureFlash : false // allow flash messages
        }));

        // SIGNUP =================================
        // show the signup form
        app.get('/signup', function(req, res) {
            res.render('signup.ejs', { message: req.flash('signupMessage') });
        });

        // process the signup form
        app.post('/signup', passport.authenticate('local-signup', {
            successRedirect : '/login', // redirect to the secure profile section
            failureRedirect : '/login', // redirect back to the signup page if there is an error
            failureFlash : true // allow flash messages
        }));

// =============================================================================
// AUTHORIZE (ALREADY LOGGED IN / CONNECTING OTHER SOCIAL ACCOUNT) =============
// REDIRECTS
// =============================================================================

        app.get('/home', isLoggedIn, function(req, res) {
            res.render('../index.html');
        });

        app.use(function(req, res, next){
          res.status(404).render('404.ejs');
        });

        app.use(function(err, req, res, next){
          console.error(err.stack);
          res.status(500).send('Irgendwas ist kaputt!');
        });
};

function wrongLoginData(){
   var l = 20;
   for( var i = 0; i < 10; i++ )
     $( "#username" ).animate( {
         'margin-left': "+=" + ( l = -l ) + 'px',
         'margin-right': "-=" + l + 'px'
      }, 50);
      $( "#password" ).animate( {
          'margin-left': "+=" + ( l = -l ) + 'px',
          'margin-right': "-=" + l + 'px'
       }, 50);
}

// route middleware to ensure user is logged in
function isLoggedIn(req, res, next) {
    console.log(req.isAuthenticated())
    if (true)//req.isAuthenticated())
        return next();

    res.redirect('/login');
}
