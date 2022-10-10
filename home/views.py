from django.shortcuts import render, redirect
from home.models import verified_weibo, unverified_weibo

# Create your views here.

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    # Waiting for the functions
    return render(request, 'home.html')

def about(request):
    # Waiting for the functions
    return render(request, 'about.html')


def main_graph(request):
    return render(request, 'main_graph.html')

def single_detection(request):
    return render(request, 'single_detection.html')

def detection0(request):
    return render(request, 'detection0.html')

def detection1(request):
    return render(request, 'detection1.html')

def detection_text(request):
    return render(request, 'detection_text.html')

def detection2(request):
    return render(request, 'detection2.html')

def detection3(request):
    return render(request, 'detection3.html')

def detection_pic(request):
    return render(request, 'detection_pic.html')

def detection4(request):
    return render(request, 'detection4.html')

def detection_comment(request):
    return render(request, 'detection_comment.html')

def edit(request):
    return render(request, 'edit.html')

def data_analyse(request):
    return render(request, 'data_analyse.html')

def unverified_database(request):
    unverified = unverified_weibo.objects.filter()
    return render(request, 'unverified_database.html', {"unverified": unverified, "dt":1})

def verified_database(request):
    verified = verified_weibo.objects.filter()
    return render(request, 'verified_database.html', {"verified": verified})

def multi_detect(request):
    a = request.POST.get("detect", None)
    b = request.POST.get("submit", None)
    c = request.POST.get("delete", None)
    e = request.POST.get("type", None)

    dt = 0


    if e:
        e = request.POST.get("weibo_id", None)
        type = request.POST.get("type", None)
        weibo = unverified_weibo.objects.get(id=e)
        verified_weibo.objects.create(username=weibo.username,
                                      content=weibo.content,
                                      public_time=weibo.public_time,
                                      img_url=weibo.img_url,
                                      zhuanfa=weibo.zhuanfa,
                                      pinglun=weibo.pinglun,
                                      dianzan=weibo.dianzan,
                                      fake_type=type, )
        weibo.delete()
        return redirect("http://127.0.0.1:8000/multi_detect")

    if b:
        b = request.POST.get("weibo_id", None)
        weibo = unverified_weibo.objects.get(id=b)
        verified_weibo.objects.create(username=weibo.username,
                                      content=weibo.content,
                                      public_time=weibo.public_time,
                                      img_url=weibo.img_url,
                                      zhuanfa=weibo.zhuanfa,
                                      pinglun=weibo.pinglun,
                                      dianzan=weibo.dianzan,
                                      fake_type=weibo.fake_type, )
        weibo.delete()

    if c:
        c = request.POST.get("weibo_id", None)
        weibo = unverified_weibo.objects.get(id=c)
        weibo.delete()

    if a:
        dt=1
        unverified_weibo.objects.create(username="3412710012471539",
                                        content="四川雅安 2013年4月20日。一男子因为LOL打团不肯离开。最后被压房下。还好网管及时救出。",
                                        public_time="2020-09-21 14:53",
                                        img_url="http://ww2.sinaimg.cn/large/b1ad5e07jw1e3yn8hrhkmj20b308cgm0.jpg",
                                        zhuanfa=410,
                                        pinglun=76,
                                        dianzan=14,
                                        fake_type="盗图新闻", )
        unverified_weibo.objects.create(username="3492710012471539",
                                        content="东北证券吉林公主岭营业部今天上午被愤怒的股民点燃.",
                                        public_time="2020-09-21 14:53",
                                        img_url="http://ww2.sinaimg.cn/large/3dc2ac30jw1dx457fr1owj.jpg",
                                        zhuanfa=14,
                                        pinglun=10,
                                        dianzan=0,
                                        fake_type="盗图新闻", )

        unverified_weibo.objects.create(username="3569866093381177",
                                        content="被和谐好几次了。继续吧。还有靠谱的人联系我。 我在:2韩国",
                                        public_time="2020-04-22 12:44",
                                        img_url="http://ww2.sinaimg.cn/large/817561d7jw1e3yakgqkalj20at097ab1.jpg",
                                        zhuanfa=18,
                                        pinglun=8,
                                        dianzan=1,
                                        fake_type="评论语义", )
        unverified_weibo.objects.create(username="3708671865257353",
                                        content="清华大学院长阎学通：与美国相比，我觉得中国早就是超级大国了：污染超级大国，腐败超级大国...",
                                        public_time="2020-05-10 13:28",
                                        img_url="http://ww3.sinaimg.cn/large/4fca5397gw1dtjjwget52j.jpg",
                                        zhuanfa=1102,
                                        pinglun=248,
                                        dianzan=75,
                                        fake_type="已知假新闻", )
        unverified_weibo.objects.create(username="3452401115729655",
                                        content="审判长先生：我作为一名三陪女，站在这个庄严的法庭上我感到羞耻。我曾给原市委书记韦君梓做过两年二奶",
                                        public_time="2020-06-02 09:20",
                                        img_url="http://ww3.sinaimg.cn/large/4fca5397gw1dtjjwget52j.jpg",
                                        zhuanfa=63,
                                        pinglun=12,
                                        dianzan=0,
                                        fake_type="已知假新闻", )
        unverified_weibo.objects.create(username="3875414273514704",
                                        content="世界那么大，那里才安全？ 2兰州·榆中县第六中学",
                                        public_time="2020-08-13 16:23",
                                        img_url="http://ww3.sinaimg.cn/large/006c4WZjjw1ev12aizvcoj30et0m8abl.jpg",
                                        zhuanfa=0,
                                        pinglun=0,
                                        dianzan=1,
                                        fake_type="盗图新闻", )
        unverified_weibo.objects.create(username="3687854410090549",
                                        content="#马航飞机失联#看完这张照片你一定会质疑到不能行！但事实在证明马来西亚在隐瞒什么！",
                                        public_time="2020-03-14 02:47",
                                        img_url="http://ww4.sinaimg.cn/large/5d6648f2jw1eeepc8d7yvj20hs0np77f.jpg",
                                        zhuanfa=22,
                                        pinglun=20,
                                        dianzan=10,
                                        fake_type="图片篡改", )
        unverified_weibo.objects.create(username="3567981999315667",
                                        content="蓄谋已久的复旦投毒。林某本想杀姜成，误杀了黄洋。",
                                        public_time="2020-09-11 22:48",
                                        img_url="http://ww1.sinaimg.cn/large/7c27db9fjw1dwsyufp10qj.jpg",
                                        zhuanfa=0,
                                        pinglun=12,
                                        dianzan=0,
                                        fake_type="已知假新闻", )
        unverified_weibo.objects.create(username="3489205663102794",
                                        content="看来中日真的要开打了！局势紧张啊！",
                                        public_time="2020-09-11 22:48",
                                        img_url="http://ww1.sinaimg.cn/large/7c27db9fjw1dwsyufp10qj.jpg",
                                        zhuanfa=16,
                                        pinglun=1,
                                        dianzan=0,
                                        fake_type="图片篡改", )
        unverified_weibo.objects.create(username="3556551304180279",
                                        content="就因为刚才那条微博，我受到了我朋友的严厉批评！",
                                        public_time="2020-03-16 18:48",
                                        img_url="http://ww3.sinaimg.cn/large/84f41de9jw1e2rtdl9g1cj.jpg",
                                        zhuanfa=147,
                                        pinglun=117,
                                        dianzan=11,
                                        fake_type="已知假新闻", )
        unverified_weibo.objects.create(username="3679006043852862",
                                        content="陕西永寿刘爱玲惨死，震动了整个永寿。原因是她家被当地政府强拆，父亲因此上访被打残关进黑监狱！",
                                        public_time="2020-02-17 16:47",
                                        img_url="http://ww4.sinaimg.cn/large/7608d41djw1edmh42il34j20bc0au0t4.jpg",
                                        zhuanfa=2,
                                        pinglun=3,
                                        dianzan=2,
                                        fake_type="已知假新闻", )
        unverified_weibo.objects.create(username="3555027400082577",
                                        content="刘丽是个普通的劳动妇女，她的良心很正，是一个能够代表人民利益的合格的“人大代表。",
                                        public_time="2020-06-13 13:09",
                                        img_url="http://ww2.sinaimg.cn/large/670ea1ecjw1e5mfir8o7zj20c80fn3zn.jpg",
                                        zhuanfa=158,
                                        pinglun=38,
                                        dianzan=8,
                                        fake_type="盗图新闻", )
        unverified_weibo.objects.create(username="3588716616221113",
                                        content="太震憾了！这是拍自四川大凉山区、贵州毕节两个贫困县儿童现状的照片。有如此破衣烂衫，中国梦又如何实现！",
                                        public_time="2020-06-13 13:09",
                                        img_url="http://ww2.sinaimg.cn/large/670ea1ecjw1e5mfir8o7zj20c80fn3zn.jpg",
                                        zhuanfa=76,
                                        pinglun=29,
                                        dianzan=1,
                                        fake_type="图片篡改", )
        unverified_weibo.objects.create(username="3506905844043560",
                                        content="2011深圳大运800亿，2010广州亚运1200亿，上海世博3000亿，2008北京奥运3000亿",
                                        public_time="2020-10-30 19:02",
                                        img_url="http://ww3.sinaimg.cn/large/6b4378a6jw1dydfnwi130j.jpg",
                                        zhuanfa=17,
                                        pinglun=9,
                                        dianzan=0,
                                        fake_type="已知假新闻", )
        unverified_weibo.objects.create(username="3875734777442426",
                                        content="中国政府公信力何在？一个没有公信力的政府能存在多久？宁可相信道听途说也不相信政府的国家还能存在多久？",
                                        public_time="2021-04-16 00:49",
                                        img_url="http://ww1.sinaimg.cn/large/b3c7dfc7jw1ev22zj858mj20lc0zktdc.jpg",
                                        zhuanfa=0,
                                        pinglun=0,
                                        dianzan=0,
                                        fake_type="盗图新闻", )
        unverified_weibo.objects.create(username="3867068636394068",
                                        content="**教委紧急通知**:牛肉不许吃了。未接到解除通知之前不许买牛肉。 钓鱼乡辉山乳液养牛场的牛生病了，牛死了人扒皮感染了炭疽病，皮肤溃烂，高烧不退。",
                                        public_time="2020-07-21 05:49",
                                        img_url="http://ww1.sinaimg.cn/large/c5796fddjw1euaft47ej6j20hs0nzq3p.jpg",
                                        zhuanfa=0,
                                        pinglun=7,
                                        dianzan=1,
                                        fake_type="盗图新闻", )

    unverified = unverified_weibo.objects.filter()
    return render(request, 'batch_detection.html', {"unverified": unverified, "dt": dt})


def multi_detail(request):
    id = request.GET.get('weibo_id', None)
    print(id)
    weibo = unverified_weibo.objects.values()
    if id:
        weibo = weibo.filter(id=id)
    return render(request, 'multi_detail.html', {"weibo": weibo})


def verified_multi_detail(request):
    id = request.GET.get('weibo_id', None)
    print(id)
    weibo = verified_weibo.objects.values()
    if id:
        weibo = weibo.filter(id=id)
    return render(request, 'verified_multi_detail.html', {"weibo":weibo})
