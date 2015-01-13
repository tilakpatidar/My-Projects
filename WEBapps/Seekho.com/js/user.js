/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(document).ready(function(){
    var content={};
    content["text"]=[];
    content["video"]=[];
    content["file"]=[];
    
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
        
             $("#warning").slideDown().show(5000,function(){$("#warning").show(5000,function(){$("#warning").slideUp(1000);});});
      
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

