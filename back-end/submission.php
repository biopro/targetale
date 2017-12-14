<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>TargeTALE: submit</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body style="height:100%">
        <div class="container">
            <nav  class="navbar navbar-expand-lg navbar-light">
                <img class="navbar-logo" src="img/dna.png">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggler" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarToggler">
                    <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                        <li class="nav-item">
                          <a class="nav-link" href="index.html">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="submit.html">Submit</a>
                        </li>
                        <li class="nav-item">
                                <a class="nav-link" href="jobs.html">Jobs</a>
                            </li>
                        <li class="nav-item">
                          <a class="nav-link" href="contact.html">Contact us</a>
                        </li>
                    </ul>
                    </div>
                    </nav>
                    <hr>

            <div class="container">
                <h3>Submit</h3>

                <p>Submit a genome to be analyzed by our pipeline. It might be a unannotated record in FASTA format (.fasta) 
                   or an already annotated record in GenBank file format (.gb, .gbk). As the analysis may take some time, 
                   you must provide an e-mail address so we may contact you at the end of the process. All results are stored 
                   for at least 1 week in our server, so we recommend you to download all finished jobs as soon as possible.
                </p>

                <?php 

                    // alert function

                    function alert ($type, $messenge){

                        $raw_alert = "<div class=\"alert %s\" role=\"alert\">%s</div>";
                        return sprintf($raw_alert, $type, $messenge);

                    };

                    // database setup

                    $mysqlHost = "localhost";
                    $mysqlUser = "root";
                    $mysqlPassword = "querocafe";

                    // database connection

                    $connection = new mysqli($mysqlHost, $mysqlUser, $mysqlPassword, 'targetale');

                    if ($connection->connect_error){
                        
                        echo (alert("alert-danger", "Error: unable to connect to the database."));

                    } else {

                        // recuperar dados de entrada

                        $userEmail = $_POST['email'];
                        $userEmail = trim($userEmail);
                        $userEmail = strtolower($userEmail);
                        $userEmailMD5 = md5($userEmail);
                        $userFileDir = '/etc/targetale/uploads/' . $userEmailMD5;

                        $tmpFilePath = $_FILES['genome']['tmp_name'];
                        $fileFormat = $_POST['file-format'];

                        $finalFilePath = $userFileDir . '/' . md5($tmpFilePath . date() . time());

                        $promoterome = $_GET['promoterome'];

                        // create a dir for the user, if it doesn't exist yet

                        if (!is_dir($userFileDir)){

                            mkdir($userFileDir);

                        };
                        
                        // save uploaded file to user file directory

                        move_uploaded_file($tmpFilePath, $finalFilePath);

                        $sql = "INSERT INTO projects (userEmail, submissionDate, status, inputFilePath, inputFileFormat, promoterome) VALUES ('$userEmail', CURDATE(), 'queued', '$finalFilePath', '$fileFormat', '$promoterome')";

                        if ($connection->query($sql) === TRUE) {

                            echo (alert("alert-success", "Your jobs was successfully submitted!"));

                        } else {

                            echo (alert("alert-danger", "Error: unable to submitting your job."));

                        }
                        
                        $connection->close();

                    }

                ?>
                
                <br>
                <h3>Cite Us</h3>
                
                <p>
                    If you have used TargeTALE on your research, please, cite the following references:
                </p>
                <p>
                    <ul> Kremer <i>et al</i> (2018). <i>A web tool to map TALE genes in the genome <i>X. oryzae</i> strains and their potential targets</i>. <b> Unpublished</b>.</ul>
                </p>

            </div>
        </div>
     
    </body>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
</html>