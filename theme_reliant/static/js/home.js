odoo.define('theme_reliant.home', function (require) {
"use strict";
    
    var ajax = require('web.ajax')


    $(document).ready(function(){

        $("p.p_reliant_project_list_2_1").click(function(){
            var id_country_filtro = $(this).attr("id");
            var selector_oculta = "div.show_init:not([id='" + String(id_country_filtro) + "'])";
            var selector_muestra = "div.show_init[id='" + String(id_country_filtro) + "']";
            $(selector_oculta).hide();
            $(selector_muestra).show();

        });

        $("p.p_reliant_project_list_2_0").click(function(){
            //var id_country_filtro = $(this).attr("id");
            var selector_muestra = "div.show_init:not([id='0'])";
            $(selector_muestra).show();
        });

        $("div.show_init_services").mouseover(function(){
            $(this).find('div.info_service_estado_1').css('background-color', '#D4FCE8')

            ajax.jsonRpc("/ajaxtocontroller", 'call', 
            { service: this.id
            },{'async':false}) 			
            .then(function (data) {

                //var obj = jQuery.parseJSON(data);
                var respons = data; //data = {"titulo_service": select_service.name_service}
                //result.push(data);
                var strhtml = '<div class="rel_snippet4_loc_service_detail">';
                strhtml += '<p class="p_reliant_service_title">' + respons.titulo_service + '</p>';
                strhtml += '<p class="p_reliant_service_description_4">' + respons.descripcion_service + '</p></div>';
                //print(strhtml)

                $(".show_init_services_2").empty(strhtml);
                $(".show_init_services_2").append(strhtml);
                $("#show_project").empty();
                data['project'].forEach(p => {
                    /*var strhtmlimg1 = '<div class="rel_snippet4_3_2 info_current_project_estado_1" data-name="Block" style="background-image: url(data:image/png;base64,' + p['imagen_project'] + '); height:376px; <width:376px;">'
                    strhtmlimg1 += '<div class="rel_snippet4_3_2_aux" style="display:none;" ><p class="p_reliant_service_title_3">' + p['nombre_project'] + '</p></div></div>'*/                                                                                                                     
                            var strhtmlimg1 ='<div class="col-4 rel_snippet4_loc show1" onmouseover="changeovershow(this)" onmouseout="changeoutshow(this)">' 
                            strhtmlimg1 +='<div class="rel_snippet4_3_2 info_current_project_estado_1" data-name="Block" style="background-image: url(data:image/png;base64,' + p['imagen_project'] + '); height:376px; <width:376px;">'
                            strhtmlimg1 +='<div class="rel_snippet4_3_2_aux" style="display:none;" ><p class="p_reliant_service_title_3">' + p['nombre_project'] + '</p></div></div>'
                            strhtmlimg1 +='</div>'
                    $("#show_project").append(strhtmlimg1);   
                });
                /*
                if (respons.imagen_project_1 !== null){
                //t-attf-style="background-image: url(data:image/png;base64,#{proj.image.decode('utf-8')}); 
                 
                }

                if(respons.imagen_project_2 !== null){
                var strhtmlimg2 = '<div class="rel_snippet4_3_2 info_current_project_estado_1" data-name="Block" style="background-image: url(data:image/png;base64,' + respons.imagen_project_2 + '); height:376px; width:376px;">'
                strhtmlimg2 += '<div class="rel_snippet4_3_2_aux" style="display:none;" ><p class="p_reliant_service_title_3">' + respons.nombre_project_2 + '</p></div></div>'

                $("#show2").empty();                
                $("#show2").append(strhtmlimg2);    
                }
                
                if(respons.imagen_project_3 !== null){
                var strhtmlimg3 = '<div class="rel_snippet4_3_2 info_current_project_estado_1" data-name="Block" style="background-image: url(data:image/png;base64,' + respons.imagen_project_3 + '); height:376px; width:376px;">'
                strhtmlimg3 += '<div class="rel_snippet4_3_2_aux" style="display:none;" ><p class="p_reliant_service_title_3">' + respons.nombre_project_3 + '</p></div></div>'    

                $("#show3").empty();
                $("#show3").append(strhtmlimg3);    
                }     
                */
            })
        });
        
        $("div.show_init_services").mouseout(function(){
            $(this).find('div.info_service_estado_1').css('background-color', '#B4B4AF')

            $(".show_init_services_2").empty();
            
        });

        $("a.btn_reliant_project").mouseover(function(){
            $(this).css('background-color', '#000000')
            $(this).css('color', '#ffffff')
        });

        $("a.btn_reliant_project").mouseout(function(){
            $(this).css('background-color', '#D4FCE8')
            $(this).css('color', '#000000')
        });

        $(".show1").mouseover(function(){
            $(this).find('div.rel_snippet4_3_2_aux').show()
            
        });

        $(".show1").mouseout(function(){
            $(this).find('div.rel_snippet4_3_2_aux').hide()
        });

        
        

        $("div.show_init").mouseover(function(){
            $(this).find('div.div_reliant_project_1').hide();
            $(this).find('div.div_reliant_project_2').show();
            $(this).find('div.div_reliant_project_3').show();  
        });

        $("div.show_init").mouseout(function(){
            $(this).find('div.div_reliant_project_1').show();
            $(this).find('div.div_reliant_project_2').hide();
            $(this).find('div.div_reliant_project_3').hide();  
        });

        $("div.show_init_home_bottom_1").mouseover(function(){
            $(this).find('div.div_name_home_bottom_1').show();
        });

        $("div.show_init_home_bottom_1").mouseout(function(){
            $(this).find('div.div_name_home_bottom_1').hide();  
        });
        $("div.show_init_home_bottom_2").mouseover(function(){
            $(this).find('div.div_name_home_bottom_2').show();
        });

        $("div.show_init_home_bottom_2").mouseout(function(){
            $(this).find('div.div_name_home_bottom_2').hide();  
        });
        $("div.show_init_home_bottom_3").mouseover(function(){
            $(this).find('div.div_name_home_bottom_3').show();
        });

        $("div.show_init_home_bottom_3").mouseout(function(){
            $(this).find('div.div_name_home_bottom_3').hide();  
        });

        $("#inputCountry").change(function(){
            var country = $(this).val()
            var department = $('#inputDepartment').val()
            var site = $('#inputSite').val()
            var language = $('#inputLanguage').val()
            
            ajax.jsonRpc("/change/job", 'call', 
            { country: country, department: department, site: site, language: language })          
            .then(function (data) {
                console.log(data['opportunities'])
                $("#job_opportunity").empty();
                data['opportunities'].forEach(opportunity => {
                    console.log(opportunity)
                    var div = '<div style="padding: 10px 0 10px 0;">'
                        div+='<div style="background-color:#C8C8C8;padding: 18px;">'
                        div+='<a  href="' + '/job_opportunities/'+opportunity['id'].toString()+'" style="text-decoration: none;">'     
                        div+='<div style="display:flex;margin: 0 0 12px 0;">'
                        div+='<div style="width:50%;font-size:15px;">'
                        div+='<div style="width: 45%;">'
                        div+='<p class="p_font_job"><strong>'+opportunity['position'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="width:30%;font-size:15px;">'
                        div+='<div style="width: 75%;">'
                        div+='<p class="p_font_job"><strong>'+opportunity['location'].toString()+'</strong> / <strong>'+opportunity['site'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="width:20%;font-size:15px;">'
                        div+='<div>'
                        div+='<p class="p_font_job"><strong>'+opportunity['closing_date'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="display:flex;margin: 0 0 12px 0;">'
                        div+='<div style="width:100%;font-size:12px;">'
                        div+='<div><p class="p_font_job">'+opportunity['category_job_opportunity'].toString()+'</p></div>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="display:flex;">'
                        div+='<div style="width:80%;font-size:12px;">'
                        div+='<div><p class="p_font_job">'+opportunity['description_job_opportunity'].toString()+'</p></div>'
                        div+='</div>'
                        div+='</div>'
                        div+='</a>'    
                        div+='</div>'
                        div+='</div>'  
                    $("#job_opportunity").append(div);
                })

            });
            
        });
        $("#inputDepartment").change(function(){
            var country = $('#inputCountry').val()
            var department = $(this).val()
            var site = $('#inputSite').val()
            var language = $('#inputLanguage').val()
            
            ajax.jsonRpc("/change/job", 'call', 
            { country: country, department: department, site: site, language: language })          
            .then(function (data) {
                console.log(data['opportunities'])
                $("#job_opportunity").empty();
                data['opportunities'].forEach(opportunity => {
                    console.log(opportunity)
                    var div = '<div style="padding: 10px 0 10px 0;">'
                        div+='<div style="background-color:#C8C8C8;padding: 18px;">'
                        div+='<a  href="' + '/job_opportunities/'+opportunity['id'].toString()+'" style="text-decoration: none;">'     
                        div+='<div style="display:flex;margin: 0 0 12px 0;">'
                        div+='<div style="width:50%;font-size:15px;">'
                        div+='<div style="width: 45%;">'
                        div+='<p class="p_font_job"><strong>'+opportunity['position'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="width:30%;font-size:15px;">'
                        div+='<div style="width: 75%;">'
                        div+='<p class="p_font_job"><strong>'+opportunity['location'].toString()+'</strong> / <strong>'+opportunity['site'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="width:20%;font-size:15px;">'
                        div+='<div>'
                        div+='<p class="p_font_job"><strong>'+opportunity['closing_date'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="display:flex;margin: 0 0 12px 0;">'
                        div+='<div style="width:100%;font-size:12px;">'
                        div+='<div><p class="p_font_job">'+opportunity['category_job_opportunity'].toString()+'</p></div>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="display:flex;">'
                        div+='<div style="width:80%;font-size:12px;">'
                        div+='<div><p class="p_font_job">'+opportunity['description_job_opportunity'].toString()+'</p></div>'
                        div+='</div>'
                        div+='</div>'
                        div+='</a>'    
                        div+='</div>'
                        div+='</div>'  
                    $("#job_opportunity").append(div);
                })

            });
            
        });
        $("#inputSite").change(function(){
            var country = $('#inputCountry').val()
            var department = $('#inputDepartment').val()
            var site = $(this).val()
            var language = $('#inputLanguage').val()
            
            ajax.jsonRpc("/change/job", 'call', 
            { country: country, department: department, site: site, language: language })          
            .then(function (data) {
                console.log(data['opportunities'])
                $("#job_opportunity").empty();
                data['opportunities'].forEach(opportunity => {
                    console.log(opportunity)
                    var div = '<div style="padding: 10px 0 10px 0;">'
                        div+='<div style="background-color:#C8C8C8;padding: 18px;">'
                        div+='<a  href="' + '/job_opportunities/'+opportunity['id'].toString()+'" style="text-decoration: none;">'     
                        div+='<div style="display:flex;margin: 0 0 12px 0;">'
                        div+='<div style="width:50%;font-size:15px;">'
                        div+='<div style="width: 45%;">'
                        div+='<p class="p_font_job"><strong>'+opportunity['position'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="width:30%;font-size:15px;">'
                        div+='<div style="width: 75%;">'
                        div+='<p class="p_font_job"><strong>'+opportunity['location'].toString()+'</strong> / <strong>'+opportunity['site'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="width:20%;font-size:15px;">'
                        div+='<div>'
                        div+='<p class="p_font_job"><strong>'+opportunity['closing_date'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="display:flex;margin: 0 0 12px 0;">'
                        div+='<div style="width:100%;font-size:12px;">'
                        div+='<div><p class="p_font_job">'+opportunity['category_job_opportunity'].toString()+'</p></div>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="display:flex;">'
                        div+='<div style="width:80%;font-size:12px;">'
                        div+='<div><p class="p_font_job">'+opportunity['description_job_opportunity'].toString()+'</p></div>'
                        div+='</div>'
                        div+='</div>'
                        div+='</a>'    
                        div+='</div>'
                        div+='</div>'   
                    $("#job_opportunity").append(div);
                })

            });
            
        });
        $("#inputLanguage").change(function(){
            var country = $('#inputCountry').val()
            var department = $('#inputDepartment').val()
            var site = $('#inputSite').val()
            var language = $(this).val()
            
            ajax.jsonRpc("/change/job", 'call', 
            { country: country, department: department, site: site, language: language })          
            .then(function (data) {
                console.log(data['opportunities'])
                $("#job_opportunity").empty();
                data['opportunities'].forEach(opportunity => {
                    console.log(opportunity)
                    var div = '<div style="padding: 10px 0 10px 0;">'
                        div+='<div style="background-color:#C8C8C8;padding: 18px;">'
                        div+='<a  href="' + '/job_opportunities/'+opportunity['id'].toString()+'" style="text-decoration: none;">'     
                        div+='<div style="display:flex;margin: 0 0 12px 0;">'
                        div+='<div style="width:50%;font-size:15px;">'
                        div+='<div style="width: 45%;">'
                        div+='<p class="p_font_job"><strong>'+opportunity['position'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="width:30%;font-size:15px;">'
                        div+='<div style="width: 75%;">'
                        div+='<p class="p_font_job"><strong>'+opportunity['location'].toString()+'</strong> / <strong>'+opportunity['site'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="width:20%;font-size:15px;">'
                        div+='<div>'
                        div+='<p class="p_font_job"><strong>'+opportunity['closing_date'].toString()+'</strong></p>'
                        div+='</div>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="display:flex;margin: 0 0 12px 0;">'
                        div+='<div style="width:100%;font-size:12px;">'
                        div+='<div><p class="p_font_job">'+opportunity['category_job_opportunity'].toString()+'</p></div>'
                        div+='</div>'
                        div+='</div>'
                        div+='<div style="display:flex;">'
                        div+='<div style="width:80%;font-size:12px;">'
                        div+='<div><p class="p_font_job">'+opportunity['description_job_opportunity'].toString()+'</p></div>'
                        div+='</div>'
                        div+='</div>'
                        div+='</a>'    
                        div+='</div>'
                        div+='</div>'   
                    $("#job_opportunity").append(div);
                })

            });
            
        });

    });
});
