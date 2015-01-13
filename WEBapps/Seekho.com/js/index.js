$(document).ready(function(){
    $('#warning').hide();
    $('#dash').hide();
    $("#accept").val("off");
    g=$('#ajax_area').html();
    click=0;
    content={};
    content["text"]=[];
    content["video"]=[];
    content["file"]=[];
});
function user(){
    $(document).ready(function(){
    
    
    $('#show_profile').css('cursor','pointer');
    $('#create_course').css('cursor','pointer');
    $('#join_course').css('cursor','pointer');
    $('#show_profile').on('click',function(){
        window.location='/cgi-bin/user.py';
        return false;
    });
    $('#join_course').on('click',function(){
        $('#user_body').html('');
         $.ajax({
				
				url: '/cgi-bin/joinedCourses.py',
				dataType:'text',
		       error: function() {
		      //test( "page not found" );
		    }
		  
		}).done(function(text){
                                $('#user_body').append(text);
				});
    
    });
    $('#create_course').on('click',function(){
        $('#user_body').html('');
        
        $('#user_body').append('<div class="container" style="width:100&percnt;;" >    <div class="row" style="padding-top:10px !important;padding-bottom:10px !important;">      <label for="course_title" class="col-lg-2 control-label">Course Title</label>      <div class="col-sm-10 col-md-10 col-lg-10">        <input type="text" class="form-control" id="course_title" placeholder="Title"/>      </div>    </div>    <div class="row" style="padding-top:10px !important;padding-bottom:10px !important;">      <label for="course_description" class="col-lg-2 control-label">Course Description</label>      <div class="col-sm-10 col-md-10 col-lg-10">        <textarea col=10 row=10 class="form-control" id="course_description" placeholder="Description"></textarea>      </div>    </div>     <div class="row" style="padding-top:10px !important;padding-bottom:10px !important;">      <label for="course_description" class="col-lg-2 control-label">Course Category</label>      <div class="col-sm-10 col-md-10 col-lg-10">        <select class="form-control" id="course_category">		  <option value="code">Code</option>		  <option value="phy">Physics</option>		  <option value="chem">Chemistry</option>		  <option value="math">Maths</option></select>      </div>    </div>    <div class="row" style="padding-top:10px !important;padding-bottom:10px !important;">      <label for="course_description" class="col-lg-2 control-label">Course Duration</label>      <div class="col-sm-10 col-md-10 col-lg-10">        <input type="text" class="form-control" id="course_duration" placeholder="Duration in minutes"/>      </div>    </div>    <div class="row" style="padding-top:10px !important;padding-bottom:10px !important;">            <div class="col-sm-10 col-md-10 col-lg-10 col-lg-offset-2" id="content_container">              </div>    </div>    <div class="row" style="padding-top:10px !important;padding-bottom:10px !important;">            <div class="col-sm-10 col-md-10 col-lg-10 col-lg-offset-2">        <button data-toggle="modal" data-target="#content_modal" class="btn btn-primary"><span class="glyphicon glyphicon-plus"></span>&nbsp;Add Content</button>      </div>    </div>        <div class="row" style="padding-top:10px !important;padding-bottom:10px !important;">      <div class="col-sm-10 col-md-10 col-lg-10 col-lg-offset-2">        <button class="btn btn-danger">Reset</button>        <button id="course_submit" class="btn btn-primary">Submit</button>      </div>    </div>     </div>');
        $("#course_submit").bind('click',function(){
       
        if($("#course_title").val()!=="" && $("#course_description").val()!==""){
        content['main']={'title':encodeURI($("#course_title").val().trim()),'description':encodeURI($("#course_description").val().trim()),'duration':encodeURI($("#course_duration").val().trim())};
        content['main']['category']=encodeURI($("#course_category").val());
        $("#user_body").html('');
        $("#user_body").html('<strong>Please wait . . . </strong>');
        $.ajax({
				type:'POST',
                                data:{query:JSON.stringify(content)},
				url: '/cgi-bin/save_course.py',
				dataType:'text',
		       error: function() {
		      //test( "page not found" );
		    }
		  
		}).done(function(text){
                                    if(text.indexOf('Success')>=0){
                                        console.log('yes');
                                        var a=text.split('Success')[1];
                                            $("#user_body").html('<strong>Course id \"'+a+'\" Submitted Successfully !</strong>');
                                            content={};
                                            content["text"]=[];
                                            content["video"]=[];
                                            content["file"]=[];
                }
				});
                                
                                
        }
        else{
            document.getElementById("warning").innerHTML="<strong>Oh!</strong> First Name required !";
        
             $("#warning").show();
      
        }
        
    });
        return false;
    });
    $("#text").on('click',function(){
        $('#content_modal').modal('hide');
        $("#text_modal").modal('show');
        
    });
     $("#file").on('click',function(){
        $('#content_modal').modal('hide');
        $("#file_modal").modal('show');
        
    });
     $("#video").on('click',function(){
        $('#content_modal').modal('hide');
        $("#video_modal").modal('show');
        
    });
     $("#text_save_btn").on('click',function(){
        $('#text_modal').modal('hide');
        var btn=$('<button class="btn btn-default"></button>');
        $('#content_container').append(btn);
        btn.text($("#text_title").val().trim());
        var obj={};
        obj['title']=encodeURI($("#text_title").val().trim());
        obj['description']=encodeURI($("#text_description").val().trim());
        obj['text']=encodeURI($("#text_save").val().trim());
        content["text"].push(obj);
        $("#text_title").val("");
        $("#text_description").val("");
        $("#text_save").val("");
        
    });
     $("#file_save_btn").on('click',function(){
        $('#file_modal').modal('hide');
        var btn=$('<button class="btn btn-default"></button>');
        $('#content_container').append(btn);
        btn.html($("#file_save").val().trim());
        var obj={};
        obj['title']=encodeURI($("#file_title").val().trim());
        obj['description']=encodeURI($("#file_description").val().trim());
        obj['link']=encodeURI($("#file_save").val().trim());
        
        content["file"].push(obj);
        $("#file_save").val("");
        $("#file_title").val("");
        $("#file_description").val("");
        
        
    });
     $("#video_save_btn").on('click',function(){
        $('#video_modal').modal('hide');
        
      var url=$("#video_save").val().trim();
          var obj={};
                var id=url.split('?v=')[1].replace('/','');//http://www.youtube.com/watch?v=2D5ZGxuAGSc
                $.ajax({
				crossDomain: true,
				url: 'https://gdata.youtube.com/feeds/api/videos/'+id+'?v=2',
				dataType:'text',
		       error: function() {
		      //test( "page not found" );
		    }
		  
		}).done(function(text){
                                
				var temp=text.split('<title>')[1];
                                obj['title']=encodeURI(temp.split('</title>')[0]);
                                temp=text.split("<media:description type='plain'>")[1];
                                obj['description']=encodeURI(temp.split("</media:description>")[0]);
                                obj['link']=encodeURI(url);
                                var btn=$(' <object data="http://www.youtube.com/embed/'+id+'" width="560" height="315"></object>');
                                 $('#content_container').append(btn);
                                 content["video"].push(obj);
                                $("#video_save").val("");
                                console.log(content);
				});
            
       
        
    });
   
    
    
});
    
}
function main(){
    $(document).ready(function(){
    
    function displayResults(val){
        
         $.ajax({
				
				url: '/cgi-bin/getSearchResults.py?query='+val,
				dataType:'text',
		       error: function() {
		      //test( "page not found" );
		    }
		  
		}).done(function(text){
                               
                                if(text==="no\n"){
                                    $("#search_results").html("");
                                    $("#search_results").append("<h2><i>No results</i></h2>");
                                }
                                else{
                                    $("#search_results").html("");
                                    $("#search_results").append(text);
                                    $(".join").on('click',function(event){
                                        var comp=$(this);
                                        $.ajax({
				
                                                        url: '/cgi-bin/joinCourse.py?id='+$(this).attr('name'),
                                                        dataType:'text',
                                               error: function() {
                                              //test( "page not found" );
                                            }

                                        }).done(function(text){
                                                        if(text.indexOf('done')>=0){
                                                            comp.attr('class','glyphicon glyphicon-ok btn btn-success');
                                                            comp.text(" Course Joined");
                                                            comp.attr('href',"javascript:alert('Already joined the course');");
						
                                                        }
                                                        else if(text.indexOf('already')>=0){
                                                            alert('Course already joined!');
                                                        }
                                                        else{
                                                            alert('Something terrible happened.Contact Developer!');
                                                        }
                                                       
                                                        });
                                        return false;
                                        
                                    });
                                }
                                    
                
				});
    }
 $("html").scroll(function() {
     
        $('html, body').animate({
            scrollTop: $("#content_body").offset().top
            }, 2000);
});

$('#subjects').click(function(){
    if(click===0){
        $('#dash').slideDown();
        
        click++;
    }
    else{
        $('#dash').slideUp();
        click=0;
    }
        
        
        return false;
    
});

function showSearchDash(){
    $('#ajax_area').html('');
    var mainrow=$('<div class="container" style="margin:0px;width:100%;height:1200px;background-color:#49bad5;"></div>');
    var row=$('<div style="height:10%;" class="row"><span>Showing results for :</span></div>');
    
    var row1=$('<div style="height:90%;" id="search_results" class="row"></div>');
    mainrow.append(row);
     mainrow.append(row1);
    
     $('#ajax_area').append(mainrow);
     row.css({
         
         'font-size':'42px',
         'font':'calibri',
         'color':'white',
         'padding':'25px'
         
         
     });
     row.children().css({
         'width':'100px',
         'text-overflow':'ellipsis',
         'word-wrap': 'break-word'
     });
    $("#search").on('keyup',function(){
     if($("#search").val().length<75){
         
                row.children().html('Showing results for :<i>'+$("#search").val().trim()+'</i>');
                if($("#search").val().trim()!=="" && $("#search").val().trim().length>2){
                    displayResults($("#search").val());
                }
                else{
                    $("#search_results").html('');
                    $("#search_results").append("<h2><i>No results</i></h2>");
                }
            
        }
        if($("#search").val().trim()===""){
        
                $('#ajax_area').html("");$('#ajax_area').append(g);
                main();
                user();
        }
        if($("#search").val().trim().length===1){
        $('#ajax_area').html('');
        showSearchDash();
    }
    });
    $("#search").on('change',function(){
     if($("#search").val().length<75){
       row.children().html('Showing results for :<i>'+$("#search").val().trim()+'</i>');
    
        }
    });
    
   
   
    
}

$("#search").on('click',function(){
    if($("#search").val().trim()===""){
        $('#ajax_area').html('');
        showSearchDash();
    }
    
});


$("#search").focusout(function(){
   
    if($("#search").val().trim()===""){
        $('#ajax_area').html("");$('#ajax_area').append(g);
        main();
        user();
        
        
        
    }
    
    
    
    
});
//signup validation part
function capitalizeMe(val){
    return val.charAt(0).toUpperCase()+val.substr(1).toLowerCase();
}
function containsChar(val)
{
    var filter=/.*[a-zA-Z]+.*/;
    if(filter.test(val))
    {
        //contains char
        return 1;
    }
    else
    {
        return 0;
        //only num
    }
}
function containsNum(jqcomp){
    var l=$(jqcomp).val().length;
    var a=0;
    var count=0;
    while(a<l)
    {
      
        var t=$(jqcomp).val().charAt(a);
        if(!isNaN(t))
        {
            count++;
            
        }
        a++;
    }
    if((count!==l)&&(count>0))
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    
    
}
function checkSpecialChar(str){
    var filter=/^\s*[a-zA-Z0-9,\s]+\s*$/;
    if (filter.test(str))
    {
        //nsp
        return 0;
    }
    else
    {
        //sp
        return 1;
    }
}

function validateEmail(sEmail) {
    var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    if (filter.test(sEmail)) {
       
        return 1;
    }
    else {
         
        return 0;
    }
}

function validateForm(){
   if(($("#inputfname").val()==="")){
      $("#warning").show();
        document.getElementById("warning").innerHTML="<strong>Oh!</strong> First Name required !";
        return false;
       
   }
   else if(($("#inputlname").val()===""))
   {
       $("#warning").show();
        document.getElementById("warning").innerHTML="<strong>Oh!</strong> Last Name required !";
       return false;
   }
   else if(($("#inputEmail").val()==="")){
       $("#warning").show();
         document.getElementById("warning").innerHTML="<strong>Oh!</strong> Email address required !";
        return false;
   }
    
    else if(($("#inputPassword").val()==="")){
     $("#warning").show();
     document.getElementById("warning").innerHTML="<strong>Oh!</strong> Password required !";
        return false;
    }
   else if(($("#rePassword").val()==="")){
       $("#warning").show();
       document.getElementById("warning").innerHTML="<strong>Oh!</strong> Confirm Password required !";
        return false;
   }
   
     else if(($("#inputUserName").val()==="")){
        $("#warning").show();
      document.getElementById("warning").innerHTML="<strong>Oh!</strong> Username required!";
      return false;
   }
   else if(($("#inputdob").val()==="")){
   $("#warning").show();
     document.getElementById("warning").innerHTML="<strong>Oh!</strong> Date of Birth required !";
     return false;
    }
    else if(($("#accept").val()==="off")){
   $("#warning").show();
     document.getElementById("warning").innerHTML="<strong>Oh!</strong> Please accept the license and agreement terms!";
     return false;
    }
   
   else
   {
      
       return true;
   }
}
$("#inputEmail").focusout(function(){
        $('#inputEmail').val($('#inputEmail').val().trim());
        $('#inputEmail').val($('#inputEmail').val().toLowerCase());
        var email= $('#inputEmail').val().toString();
        if(($("#inputPassword").val()===$("#inputEmail").val())&&($("#inputEmail").val()!==""))
        {
            $("#warning").show();
           
            document.getElementById("warning").innerHTML="Password must not be same as username or email.";
            $("#inputPassword").val("");
            $("#rePassword").val("");
            $("#inputEmail").val("");
        }
         else if(validateEmail(email)===0){
            $('#inputEmail').val('');
             $("#warning").show();
             document.getElementById("warning").innerHTML="Please enter a valid email address !";
        }
        else
        {
            $("#warning").hide();
            document.getElementById("warning").innerHTML="Please enter a valid email address !";
        }
        
    });

$("#inputfname").focusout(function(){
       
       $('#inputfname').val($('#inputfname').val().trim());
         $('#inputfname').val(capitalizeMe($('#inputfname').val()));
       
        if(((checkSpecialChar( $('#inputfname').val())===1)||(($("#inputfname").val().length)>45))||((containsNum("#inputfname")===1)||(!isNaN($('#inputfname').val()))))
        {
            $("#warning").show();
            document.getElementById("warning").innerHTML="First Name must be max 40 characters long and must not contain[0-9][!-)]";
            $('#inputfname').val('');
        }
       
        else{
              $("#warning").hide();
              document.getElementById("warning").innerHTML="First Name must be max 40 characters long and must not contain[0-9][!-)]";
        }
    });


$("#inputlname").focusout(function(){
        $('#inputlname').val($('#inputlname').val().trim());
          $('#inputlname').val(capitalizeMe($('#inputlname').val()));
         if(((checkSpecialChar( $('#inputlname').val())===1)||(($("#inputlname").val().length)>40))||((containsNum("#inputlname")===1)||(!isNaN($('#inputlname').val()))))
        {
            $("#warning").show();
             document.getElementById("warning").innerHTML="Last Name must be max 40 characters long and must not contain[0-9][!-)]";
            $('#inputlname').val('');
        }
        
        else{
              $("#warning").hide();
              document.getElementById("warning").innerHTML="Last Name must be max 45 characters long and must not contain[0-9][!-)]";
        }
    });
$("#inputUserName").focusout(function(){
        
        $("#inputUserName").val($("#inputUserName").val().trim());
        $('#inputUserName').val($('#inputUserName').val().toLowerCase());
        if($("#inputUserName").val()==="")
        {
            $("#warning").hide();
        }
        else if(($("#inputPassword").val()===$("#inputUserName").val()))
        {
            $("#warning").show();
           
            document.getElementById("warning").innerHTML="Password must not be same as username or email.";
            $("#inputPassword").val("");
            $("#rePassword").val("");
            $("#inputUserName").val("");
        
        }
        else if(containsChar($("#inputUserName").val())===0)
        {
            $("#inputUserName").val("");
            $("#warning").show();
            document.getElementById("warning").innerHTML="Username must contain atleast one character.";
        }
	
        
        else if($("#inputUserName").val()!=="")
        {
        $("#warning").hide();
        
                        
                          
                           
        }   
        
       
    });
    $("#inputPassword").focusout(function(){
         if((($("#inputPassword").val()===$("#inputUserName").val()))&&($("#inputPassword").val()!==""))
        {
            $("#warning").show();
           
            document.getElementById("warning").innerHTML="Password must not be same as username or email.";
            $("#inputPassword").val("");
            $("#rePassword").val("");
            $("#inputUserName").val("");
        
        }
        else if((($("#inputPassword").val()===$("#inputEmail").val()))&&($("#inputPassword").val()!==""))
        {
            $("#warning").show();
           
            document.getElementById("warning").innerHTML="Password must not be same as username or email.";
            $("#inputPassword").val("");
            $("#rePassword").val("");
            $("#inputEmail").val("");
        }
        else if((($("#inputPassword").val().length)>=8)&&(containsNum("#inputPassword")===1))
        {
          //fav cond
           $("#warning").hide();
           
           document.getElementById("warning").innerHTML="Password must be alpha-numeral and minimum 8 characters in length.";
           $("#rePassword").removeAttr("disabled");
           //$("#rePassword").val('');
           if($("#inputPassword").val().toString()!==$("#rePassword").val().toString())
                     {
                         document.getElementById("warning").innerHTML="Passwords do not match !";
                        
                         $("#rePassword").val("");
                     }
           $("#rePassword").focus();
                        
        }
        
        else{
             $("#inputPassword").val('');
             $("#warning").show();
              document.getElementById("warning").innerHTML="Password must be alpha-numeral and minimum 8 characters in length.";
              
        }
    });
    $("#rePassword").focusout(function(){
        if($("#inputPassword").val()===""){
             document.getElementById("warning").innerHTML="Please enter the password first !";
             $("#rePassword").val("");
            $("#warning").show();
        }
        else if($("#rePassword").val()===$("#inputPassword").val())
        {
         //pswd matched
            document.getElementById("warning").innerHTML="Passwords matched successfully !";
           $("#warning").attr("class","alert alert-success");
            $("#warning").show().hide(5000,function(){
                                   $("#warning").attr("class","alert alert-danger");
                                });
           
        }
        else{
            $("#inputPassword").val('');
            $("#rePassword").val('');
            document.getElementById("warning").innerHTML="Passwords do not match !";
            
            $("#warning").show();
             //pswd do not match
        }
    });
    $("#accept").change(function(){
       
        if($("#accept").val()==="off")
        {
            $("#accept").val("on");
           
        }
        else if($("#accept").val()==="on")
        {
            $("#accept").val("off");
            
        }
        
    });
    $('#signup_modal').on('hidden.bs.modal', function () {
        $("#warning").hide();
});
     $('#signup').on('submit', function() {

                  return validateForm();

                });
                
                
     //login form
     
     
     $("#pswd").focusout(function(){

                    if((($("#pswd").val().length)>=8)&&(containsNum("#pswd")===1))
                    {

                       $("#warning").hide();
                        document.getElementById("warning").innerHTML="<strong>Oh!</strong> Password format is wrong!";
                       
                    }
                    else{
                         $("#pswd").val('');
                         $("#warning").show();
                         document.getElementById("warning").innerHTML="<strong>Oh!</strong> Password format is wrong!";
                        
                    }
                });
                
                
                $("#uname").focusout(function(){
                   
                   if($("#uname").val().length>40)
                   {
                       $("#uname").val('');
                      $("#warning").show();
                      document.getElementById("warning").innerHTML="<strong>Oh!</strong> Username must be max 40 characters in length.";
                   }
                   else
                   {
                       $("#warning").hide(); 
                        document.getElementById("warning").innerHTML="<strong>Oh!</strong> Username must be max 40 characters in length.";
                   }
               });
               
               function validateLogin(){
                 if($("#uname").val()===""){
                    document.getElementById("warning").innerHTML="<strong>Oh!</strong> Username cannot be left blank.";         
                    $("#warning").show();
                    
                     return false;
                 }
                 else if($("#pswd").val()==="")
                 {
                     document.getElementById("warning").innerHTML="<strong>Oh!</strong> Password cannot be left blank."; 
                     $("#warning").show();
                    
                     return false;
                 }
                 else{
                      $("#warning").hide();
                    
                   
                     return true;
                 }
             }
               $('#login_frm').submit( function() {
                   
                return validateLogin();
         
     });
             //for showCourses.py   
        $(".join").on('click',function(event){
                                        var comp=$(this);
                                        $.ajax({
				
                                                        url: '/cgi-bin/joinCourse.py?id='+$(this).attr('name'),
                                                        dataType:'text',
                                               error: function() {
                                              //test( "page not found" );
                                            }

                                        }).done(function(text){
                                                        if(text.indexOf('done')>=0){
                                                            comp.attr('class','glyphicon glyphicon-ok btn btn-success');
                                                            comp.text(" Course Joined");
                                                            comp.attr('href',"javascript:alert('Already joined the course');");
                                                            var t=text.split('<username>')[1];
                                                            var username=t.split('</username>')[0];
                                                            $("#users_joined").html("");
                                                            $("#users_joined").append('<li class="list-group-item">'+username+'</li>');
                                                        }
                                                        else if(text.indexOf('already')>=0){
                                                            alert('Course already joined!');
                                                        }
                                                        else{
                                                            alert('Something terrible happened.Contact Developer!');
                                                        }
                                                       
                                                        });
                                        return false;
                                        
                                    });
           $("#comment_save").on('click',function(){
               
               
                handler();
               
           });
           $(".like").on('click',function(){
               
               console.log('clickkk');
                like_handler(this);
               
           });
      function handler(){
          if($("#comment_text").val().trim()!==""){
                   $.ajax({
				type:'POST',
                                data:{query:encodeURI($("#comment_text").val().trim()),id:encodeURI($("#comment_text").attr('name').trim())},
				url: '/cgi-bin/save_comment.py',
				dataType:'text',
		       error: function() {
		      //test( "page not found" );
		    }
		  
		}).done(function(text){
                                    if(text.indexOf('###success###')>=0){
                                        if($("#no_comment")){
                                            $("#no_comment").remove();
                                             }
                                        var t=text.replace('###success###','');
                                        $("#comment_body").html("");
                                     $("#comment_body").append(t+'<div class="container" style="width:100&percnt;;">						<div class="row" style="width:100&percnt;;">						<div class="col-lg-12" style="width:100&percnt;;">						<div class="well">														    <h4>Leave a Comment:</h4>								    									<div>									    <textarea name="%s" id="comment_text" class="form-control" rows="3"></textarea>									</div>									<button id="comment_save" class="btn btn-primary">Submit</button>								   								</div>						</div>						</div>');
                                     $("#comment_save").on('click',function(){


                                            handler();

                                       });
                
                }
                                else if(text.indexOf("###not logged in###")>=0){
                                    $("#comment_text").val("");
                                    alert("Please log in to comment !");
                                }
				});
                    
               }
      }
       function like_handler(a){
          if($(a).attr('class').indexOf('like')>=0){
                   $.ajax({
				type:'POST',
                                data:{id:encodeURI($(a).attr('name').trim())},
				url: '/cgi-bin/like_comment.py',
				dataType:'text',
		       error: function() {
		      //test( "page not found" );
		    }
		  
		}).done(function(text){
                                    if(text.indexOf('###success###')>=0){
                                        $(a).attr('class',$(a).attr('class').replace('like','liked').replace('glyphicon-thumbs-up','glyphicon-ok'));
                                        $(a).text('Liked');
                                       $(".like").on('click',function(){


                                            like_handler();

                                       });
                
                }
                                else if(text.indexOf("###not logged in###")>=0){
                                    
                                    alert("Please log in to like !");
                                }
				});
                    
               }
      }
});
   
}

main();
user(); 