$(function(){


    $('.comment_list_con').delegate('a,input','click',function(){

        var sHandler = $(this).prop('class');

        // 显示选中回复框,隐藏其他回复框
        if(sHandler.indexOf('comment_reply')>=0)
        {
            var reply_form = $(this).parent().parent().parent().find(".reply_form");
            var other_reply_form = $(this).parent().parent().parent().parent().find(".reply_form");
            other_reply_form.hide();
            reply_name = $(this).parent().find(".name").html();
            if (reply_name){
                reply_form.find(".reply_input").attr("placeholder", "@" + reply_name + "：");
            }else {
                reply_form.find(".reply_input").attr("placeholder", "发表你的评论");
            }

            reply_form.find(".reply_input").val("");
            reply_form.show();
        }


        if(sHandler.indexOf('reply_cancel')>=0)
        {
            $(this).parent().toggle();
        }

        if(sHandler.indexOf('comment_like')>=0)
        {
            var $this = $(this);
            if(sHandler.indexOf('fa-thumbs-up')>=0)
            {
                // 如果当前该评论已经是点赞状态，再次点击会进行到此代码块内，代表要取消点赞
                $this.removeClass('fa-thumbs-up')
                $this.addClass('fa-thumbs-o-up')
            }else {
                $this.addClass('fa-thumbs-up')
            }
        }

        if(sHandler.indexOf('reply_sub')>=0)
        {
            // 取到用户输入的内容.children("first-child") .
            var $this_form = $(this).parent();
            var parent_id = $this_form.parent(".comment_list").find(".user_name").attr("comment_id");
            var article_id = $this_form.parent().parent().parent().attr("news_id");
            var name = $this_form.find(".name").val();
            var email = $this_form.find(".email").val();
            var url = $this_form.find(".url").val();
            var content = $this_form.find(".reply_input").val();
            var csrf_token = $this_form.find(".csrf_token").val();
            if (!article_id){
                $this_form.find(".error").html("新闻不存在！");
                $this_form.find(".error").show();
                return;
            }
            if (!name){
                $this_form.find(".error").html("请输入昵称！");
                $this_form.find(".error").show();
                return;
            }
            if (!email){
                $this_form.find(".error").html("请输入邮箱！");
                $this_form.find(".error").show();
                return;
            }
            if (!url){
                $this_form.find(".error").html("请输入url！");
                $this_form.find(".error").show();
                return;
            }
            if (!content){
                $this_form.find(".error").html("请输入回复内容！");
                $this_form.find(".error").show();
                return;
            }

            var comment = {
                "article_id": article_id,
                "parent_id": parent_id,
                "name": name,
                "email": email,
                "url": url,
                "content": content,
                "reply_name": reply_name
            };
            $.ajax({
                url: '/comment',
                type: 'POST',
                // 把js对象转换为json格式
                data: JSON.stringify(comment),
                contentType: 'application/json',
                headers: {
                    "X-CSRFToken": csrf_token
                },
                success: function (resp) {
                 if(resp.state == "ok"){
                         $this_form.find(".error").hide();
                         $this_form.hide();
                         if(!parent_id){
                             var comment_list_con = $(".comment_list_con");
                             var comment_list = '';
                             comment_list = '<div class="comment_list">';
                             comment_list += '<div class="col-md-12">';
                             comment_list += '<div class="parent_comment">';
                             comment_list += '<div class="person_pic fl">';
                             comment_list += '<img src="../../static/img/cat.jpg" alt="用户图标">';
                             comment_list += '</div>';
                             comment_list += '<div>';
                             comment_list += '<div class="col-md-8 user_name fl name" comment_id="'+ resp.comment_id +'">'+name+'</div>';
                             comment_list += '<div class="col-md-8 comment_time fl">'+ resp.comment_time +'</div>';
                             comment_list += '</div>';
                             comment_list += '<div class="col-md-12 comment_text fl">';
                             comment_list += '<p>'+content+'</p>';
                             comment_list += '</div>';
                             comment_list += '<a href="javascript:;" class="fa fa-comment comment_reply fl">回复</a>';
                             comment_list += '<a href="javascript:;" class="fa fa-thumbs-o-up comment_like fl">0</a>';
                             comment_list += '</div>';
                             comment_list += '</div>';
                             comment_list += '<div class="col-md-10 reply_text_con fl">';
                             comment_list += '</div>';
                             comment_list += '<from class="reply_form">';
                             comment_list += '<input type="text" placeholder="昵称" class="name_email_url name">';
                             comment_list += '<input type="text" placeholder="邮箱" class="name_email_url email">';
                             comment_list += '<input type="text" placeholder="url" class="name_email_url url">';
                             comment_list += '<textarea  class="reply_input" ></textarea>';
                             comment_list += '<input type="submit" name="" value="回复" class="reply_sub fr">';
                             comment_list += '<input type="reset" name="" value="取消" class="reply_cancel fr">';
                             comment_list += '<p class="col-md-10 error"></p>';
                             comment_list += '<input type="hidden" class="csrf_token" value="'+csrf_token+'">';
                             comment_list += '</from>';
                             comment_list += '</div>';
                             $(".comment_list_con").append(comment_list);
                             alert("回复成功");
                         }
                         else {
                             var child_comment_list = $this_form.prev();
                             var child_comment = '';
                             child_comment+='<div class="child_comment">';
                             child_comment+='<div>';
                             child_comment+='<a href="#" class="user_name2 name" comment_id='+ resp.comment_id +'">'+name+'</a>@';
                             child_comment+='<a href="#" class="user_name2">'+reply_name+'</a>：';
                             child_comment+='<span class="reply_text">';
                             child_comment+=content;
                             child_comment+='</span>';
                             child_comment+='</div>';
                             child_comment+='<span class="comment_time">'+resp.comment_time+'</span>';
                             child_comment+='<a href="javascript:;" class="fa fa-comment son_comment_reply">回复</a>';
                             child_comment+='</div>';
                             child_comment_list.append(child_comment);
                             alert("回复成功");
                         }

                     }else{
                         alert(resp.state)
                     }
                 },
                 error: function(){
                    alert('回复失败');
                 },
            })


        }
    })

});