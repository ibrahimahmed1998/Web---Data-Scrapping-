<?php
 
 include('php/simple_html_dom.php');
 	 
    $url = 'http://ppndo.com/store/';
    $html = file_get_html($url);
	 
  foreach($html->find('h4') as $span) {
	
	  if($span->class == "text-info"){
       echo "Name: " . strip_tags($span)  ;
	   echo "<br>" ;
	  }
	   
	  if($span->class == "text-danger"){
       echo "Price: " . strip_tags($span)  ;
	   echo "<br>" ;
	   echo "<br>" ;
	  }
	  
  }


?>