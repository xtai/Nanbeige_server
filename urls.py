from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'nbg.views.doc_html'),

    (r'^newsfeed/$', 'nbg.views_newsfeed.newsfeed'),

    (r'^app/version/api/$', 'nbg.views_app.version_api'),
    (r'^app/version/android/$', 'nbg.views_app.version_android'),
    (r'^app/version/ios/$', 'nbg.views_app.version_ios'),
    (r'^app/notice/$', 'nbg.views_app.notice'),

    (r'^user/$', 'nbg.views_user.get_user'),
    (r'^user/login/email/$', 'nbg.views_user.login_email'),
    (r'^user/login/weibo/$', 'nbg.views_user.login_weibo'),
    (r'^user/login/renren/$', 'nbg.views_user.login_renren'),
    (r'^user/reg/(email|weibo|renren)/$', 'nbg.views_user.reg'),
    (r'^user/edit/$', 'nbg.views_user.edit'),
    (r'^user/logout/$', 'nbg.views_user.logout'),
    (r'^user/deactivate/$', 'nbg.views_user.deactivate'),

    (r'^university/$', 'nbg.views_university.university_list'),
    (r'^university/(\d+)/$', 'nbg.views_university.detail'),
    (r'^university/(\d+)/semester/$', 'nbg.views_university.semester'),
    (r'^university/semester/(\d+)/weekset/$', 'nbg.views_university.weekset'),

    (r'^course/$', 'nbg.views_course.course_list'),
    (r'^course/(\d+)/$', 'nbg.views_course.course'),
    (r'^course/(\d+)/users/$', 'nbg.views_course.course_users'),
    (r'^course/all/$', 'nbg.views_course.all'),
    (r'^course/ical/$', 'nbg.views_course.gen_ical'),
    (r'^course/(\d+)/edit/$', 'nbg.views_course.edit'),
    (r'^course/(\d+)/comment/$', 'nbg.views_course.comment_list'),
    (r'^course/(\d+)/comment/add/$', 'nbg.views_course.comment_add'),
    (r'^course/grabber/$','nbg.views_course.course_grab'),
    (r'^course/grabber/captcha/$', 'nbg.views_course.captcha_img'),
    (r'^course/grabber/start/$', 'nbg.views_course.course_grab_start'),

    (r'^comment/$', 'nbg.views_comment.comment_list'),

    (r'^study/building/$', 'nbg.views_study.building_list'),
    (r'^study/building/(\d+)/room/$', 'nbg.views_study.room_list'),

    (r'^event/$','nbg.views_event.query'),
    (r'^event/category/$','nbg.views_event.category'),
    (r'^event/(\d+)/$','nbg.views_event.event'),
    (r'^event/(\d+)/edit/$','nbg.views_event.edit'),
    (r'^event/following/$','nbg.views_event.following'),

    (r'^wiki/(\d+)/$', 'nbg.views_wiki.wiki_list'),
    (r'^wiki/node/(\d+)/$', 'nbg.views_wiki.wiki_node'),
)
