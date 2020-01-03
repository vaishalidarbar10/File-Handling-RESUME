v = open("vaishali.html","w")
c = """<!doctype html>
<html>
 <head>
<title>RESUME</title>
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">

<style type="text/css">
    table {
        font-size: 18px;
    }
    #heading{
        font-size: 20px;
        }
</style>
</head>
<body style="padding-top: 5%; padding-left:15%; padding-right:15%; ">
    <div class="col-xs-6"  >

<div >
  <center><h1><u><b> RESUME</u></b></h1></center>  
<h3>Vaishali Darbar</h3>
<p > vaishalidarbar0429@gamil.com</p>
<p>DOB: 05/01/2000</p>
<p>Adress : Indira Gandhi Girls Hostel Bhopal</p
<p>Contact No.:  6263797978</p>
 
  <h3><u><b>CAREER OBJECTIVE</u></b></h3>
  <p>To secure a position where I can efficiently contribute my skills and abilities to the growth of the organization and build my professional career.</p>
            <h3><u><b>EDUCATION </b></u></h3>
            <table border="1" class="table ">
                <tr class="table-primary">
                    <th>Qualification</th>
                    <th>Institute</th>
                    <th>Percentage / Grades</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>10th</td>
                    <td>Govt. Girls High Secondary School Rajpur.</td>
                    <td>66%</td>
                    <td>2015</td>
                </tr>
              
                <tr>
                    <td>Polytechnic</td>
                    <td> Polytechnic College Khargone MP</td>
                    <td>66 cgpa</td>
                    <td>2019</td>
                </tr>
                
            </table>

        </div>
          <h3 style="text-transform: uppercase;"><u>Key Skills</u></h3>
     <ol>
   <h3><li> C</h3>
        <div class="progress progress-striped">
        <div class="progress-bar" aria-vlauenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 70%; background-color: green;"></div>
         </div></li>

         <h3 style="text-transform: uppercase;"><li> html</h3>
                 <div class="progress">
                 <div class="progress-bar progress-bar-successs" role="progressbar" aria-vlauenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 56%; background-color: green;"></div></div>
</li>
 <h3><li> MySql</h3>
                <div class="progress">
                <div class="progress-bar progress-bar-successs" role="progressbar" aria-vlauenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 75%; background-color: green;"></div>
</div>
</li>     
        </ol>

    <h3><b><u style="text-transform: uppercase;">Langauges</u></b></h3>
    <ol style="font-size: 25px;">
        <li> English</li>
        <li>Hindi</li>
    </ol>
    <h3><u><b style="text-transform: uppercase;">Persnol Profile ID</b></u></h3>
    <ol style="font-size: 25px;">
        <li>Github :  vaishalidarbar</a></li>
        <li>Linkdin :  vaishalidarbar0429@gamil.com</a></li>
       <li>HackerRank :vaishalidarbar0429@gamil.com</a></li>
       <li>Canvas :  vaishalidarbar0429@gamil.com</a></li> 
       <li>Intershala :  vaishalidarbar</a></li></ol>    
        <h3><u><b>WORK  EXPERIENCE</u></b></h3>
        <p style="font-size: 20px;">Fresher</p>
</div></body>
</html>"""

v.write(c)
v.close()