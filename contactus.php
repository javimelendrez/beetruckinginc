<?php
// PHP code goes here
if(isset($_POST['submti'])){
    //collect data from contact form
    $name = $_POST['usr'];
    $phone = $_POST['phone'];
    $email = $_POST['email'];
    $message = $_POST['message'];


    $mailTo = "javimelendrez@icloud.com";
    $headers = "From: ".$email;
    $txt = "You have received an e-mail from ".$name.". \n\n Phone: ".$phone."\n\n".$message;

    //mail function

    mail($mailTo, $name, $txt, $headers);
    header("Location: index.php?mailsend");

    
}
?> 