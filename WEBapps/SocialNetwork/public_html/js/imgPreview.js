function readURL(input) {
     
            if(fileSelectHandler()===1){
            
            if (input.files && input.files[0]) {
                        var reader = new FileReader();

                        reader.onload = function (e) {
                            $('#img')
                                .attr('src', e.target.result)
                                .width(160)
                                .height(100);
                        };
                          
                        reader.readAsDataURL(input.files[0]);
                        $("#file_choosen").val("1");
                    
            }
            
            
           }
            
        }
