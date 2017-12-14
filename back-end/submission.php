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

                    echo $_POST["email"];

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