from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests
import googleapiclient.discovery
import scrapetube
import pafy
import pandas as pd
from sqlalchemy import create_engine
import os
import certifi
import pymysql
import pymongo
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/youtuberdata', methods=['POST', 'GET'])  # route to show the youtube videos details
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            name_or_url = request.form["content"]
            # For returning youtuber's details with latest 50 videos
            if name_or_url.replace(" ","").lower() == "krishnaik" or name_or_url == "https://www.youtube.com/user/krishnaik06":
                videos = scrapetube.get_channel(channel_url="https://www.youtube.com/user/krishnaik06", limit=50,sort_by="newest")
                krish_final_result = []
                for video in videos:
                    publish_date=video["publishedTimeText"]["simpleText"]
                    url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                    video = pafy.new(url)
                    view_count=video.viewcount
                    youtuber_name=video.author
                    duration=video.duration
                    thumbnail_link=video.bigthumbhd
                    title=video.title
                    likes_count=video.likes
                    mydict = {"Youtuber_Name": youtuber_name, "Title": title, "View_Count": view_count,
                              "Duration": duration,
                              "Likes_Count": likes_count, "Video_Link": url, "Thumbnail_Link": thumbnail_link,
                              "Published": publish_date}
                    krish_final_result.append(mydict)
                return render_template('result.html', reviews=krish_final_result[0:(len(krish_final_result))])

            if name_or_url.replace(" ","").lower() == "hiteshchoudhary" or name_or_url == "https://www.youtube.com/c/HiteshChoudharydotcom":
                videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/HiteshChoudharydotcom", limit=50,sort_by="newest")
                hitesh_final_result = []
                for video in videos:
                    publish_date = video["publishedTimeText"]["simpleText"]
                    url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                    video = pafy.new(url)
                    view_count = video.viewcount
                    youtuber_name = video.author
                    duration = video.duration
                    thumbnail_link = video.bigthumbhd
                    title = video.title
                    likes_count = video.likes
                    mydict = {"Youtuber_Name": youtuber_name, "Title": title, "View_Count": view_count,
                              "Duration": duration,
                              "Likes_Count": likes_count, "Video_Link": url, "Thumbnail_Link": thumbnail_link,
                              "Published": publish_date}
                    hitesh_final_result.append(mydict)

                return render_template('result.html', reviews=hitesh_final_result[0:(len(hitesh_final_result))])
            if name_or_url.replace(" ","").lower() == "telusko" or name_or_url == "https://www.youtube.com/c/Telusko":
                videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/Telusko", limit=50, sort_by="newest")
                telusko_final_result = []
                for video in videos:
                    publish_date = video["publishedTimeText"]["simpleText"]
                    url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                    video = pafy.new(url)
                    view_count = video.viewcount
                    youtuber_name = video.author
                    duration = video.duration
                    thumbnail_link = video.bigthumbhd
                    title = video.title
                    likes_count = video.likes
                    mydict = {"Youtuber_Name": youtuber_name, "Title": title, "View_Count": view_count,
                              "Duration": duration,
                              "Likes_Count": likes_count, "Video_Link": url, "Thumbnail_Link": thumbnail_link,
                              "Published": publish_date}
                    telusko_final_result.append(mydict)
                return render_template('result.html', reviews=telusko_final_result[0:(len(telusko_final_result))])
            if name_or_url.replace(" ","").lower() == "mysirg" or name_or_url == "https://www.youtube.com/user/saurabhexponent1":
                videos = scrapetube.get_channel(channel_url="https://www.youtube.com/user/saurabhexponent1", limit=50, sort_by="newest")
                mysirg_final_result = []
                for video in videos:
                    publish_date = video["publishedTimeText"]["simpleText"]
                    url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                    video = pafy.new(url)
                    view_count = video.viewcount
                    youtuber_name = video.author
                    duration = video.duration
                    thumbnail_link = video.bigthumbhd
                    title = video.title
                    likes_count = video.likes
                    mydict = {"Youtuber_Name": youtuber_name, "Title": title, "View_Count": view_count,
                              "Duration": duration,
                              "Likes_Count": likes_count, "Video_Link": url, "Thumbnail_Link": thumbnail_link,
                              "Published": publish_date}
                    mysirg_final_result.append(mydict)
                return render_template('result.html', reviews=mysirg_final_result[0:(len(mysirg_final_result))])

        except Exception as e:
            return e

@app.route('/mys', methods=['POST', 'GET'])  # route to uplod data to mysql database
@cross_origin()
def my_sql():
    if request.method == 'POST':
        try:
            list_ = request.form["my_sql"].split(" ")
            user = list_[0]
            password = list_[1]
            host = list_[2]
            port = list_[3]
            database = list_[4]
            db = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
            # Krish Naik's Youtube DataFrame
            try:
                videos = scrapetube.get_channel(channel_url="https://www.youtube.com/user/krishnaik06", limit=50, sort_by="newest")
            except Exception as e:
                return e
            publish_date = []
            view_count = []
            youtuber_name = []
            duration = []
            thumbnail_link = []
            video_link = []
            title = []
            likes_count = []
            vid_url = []
            try:
                for video in videos:
                    publish_date.append(video["publishedTimeText"]["simpleText"])
                    vid_url.append("https://www.youtube.com/watch?v=" + str(video["videoId"]))
                    url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                    video = pafy.new(url)
                    view_count.append(video.viewcount)
                    youtuber_name.append(video.author)
                    duration.append(video.duration)
                    thumbnail_link.append(str(video.bigthumbhd))
                    video_link.append(video.watchv_url)
                    title.append(video.title)
                    likes_count.append(video.likes)
            except:
                pass
            mydict = {}
            mydict = {"Youtuber_Name": youtuber_name, "Title": title, "View_Count": view_count, "Duration": duration,
                      "Likes_Count": likes_count, "Video_Link": video_link, "Thumbnail_Link": thumbnail_link,
                      "Published": publish_date}
            krish_df = pd.DataFrame.from_dict(mydict)

            # Hitesh Choudhary's Youtube DataFrame
            videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/HiteshChoudharydotcom", limit=50,
                                            sort_by="newest")
            publish_date = []
            view_count = []
            youtuber_name = []
            duration = []
            thumbnail_link = []
            video_link = []
            title = []
            likes_count = []
            for video in videos:
                publish_date.append(video["publishedTimeText"]["simpleText"])
                vid_url.append("https://www.youtube.com/watch?v=" + str(video["videoId"]))
                url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                video = pafy.new(url)
                view_count.append(video.viewcount)
                youtuber_name.append(video.author)
                duration.append(video.duration)
                thumbnail_link.append(str(video.bigthumbhd))
                video_link.append(video.watchv_url)
                title.append(video.title)
                likes_count.append(video.likes)

            mydict = {}
            mydict = {"Youtuber_Name": youtuber_name, "Title": title, "View_Count": view_count, "Duration": duration,
                      "Likes_Count": likes_count, "Video_Link": video_link, "Thumbnail_Link": thumbnail_link,
                      "Published": publish_date}
            hitesh_df = pd.DataFrame.from_dict(mydict)

            ##Telusko's Youtube DataFrame
            videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/Telusko", limit=50, sort_by="newest")
            publish_date = []
            view_count = []
            youtuber_name = []
            duration = []
            thumbnail_link = []
            video_link = []
            title = []
            likes_count = []
            for video in videos:
                publish_date.append(video["publishedTimeText"]["simpleText"])
                vid_url.append("https://www.youtube.com/watch?v=" + str(video["videoId"]))
                url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                video = pafy.new(url)
                view_count.append(video.viewcount)
                youtuber_name.append(video.author)
                duration.append(video.duration)
                thumbnail_link.append(str(video.bigthumbhd))
                video_link.append(video.watchv_url)
                title.append(video.title)
                likes_count.append(video.likes)

            mydict = {}
            mydict = {"Youtuber_Name": youtuber_name, "Title": title, "View_Count": view_count, "Duration": duration,
                      "Likes_Count": likes_count, "Video_Link": video_link, "Thumbnail_Link": thumbnail_link,
                      "Published": publish_date}
            telusko_df = pd.DataFrame.from_dict(mydict)

            ## MySirG's Youtube DataFrame
            videos = scrapetube.get_channel(channel_url="https://www.youtube.com/user/saurabhexponent1", limit=50, sort_by="newest")
            publish_date = []
            view_count = []
            youtuber_name = []
            duration = []
            thumbnail_link = []
            video_link = []
            title = []
            likes_count = []
            for video in videos:
                publish_date.append(video["publishedTimeText"]["simpleText"])
                vid_url.append("https://www.youtube.com/watch?v=" + str(video["videoId"]))
                url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                video = pafy.new(url)
                view_count.append(video.viewcount)
                youtuber_name.append(video.author)
                duration.append(video.duration)
                thumbnail_link.append(str(video.bigthumbhd))
                video_link.append(video.watchv_url)
                title.append(video.title)
                likes_count.append(video.likes)


            mydict = {}
            mydict = {"Youtuber_Name": youtuber_name, "Title": title, "View_Count": view_count, "Duration": duration,
                      "Likes_Count": likes_count, "Video_Link": video_link, "Thumbnail_Link": thumbnail_link,
                      "Published": publish_date}
            mysirg_df = pd.DataFrame.from_dict(mydict)


            # Final Comprehensive DataFrame
            final_df=pd.concat([krish_df, hitesh_df,telusko_df,mysirg_df], axis=0)
            # Creating youtuber's table in MySQL
            final_df.to_sql(name="video_details",con=db,if_exists="replace",index=False)
            return render_template('index.html')

        except Exception as e:
            return e


@app.route('/mongo', methods=['POST', 'GET'])  # route to upload comments and thumbnail images to mongodb
@cross_origin()
def vid():
    try:
        if request.method == 'POST':
            try:
                list_ = request.form["vid"]
                client = pymongo.MongoClient(list_,tlsCAFile=certifi.where())
                datab = client.youtube
                try:
                    datab.comments.drop()
                    datab.image.drop()

                    # getting videos url
                    videos = scrapetube.get_channel(channel_url="https://www.youtube.com/user/krishnaik06",
                                                    limit=50, sort_by="newest")
                    vid_id = []
                    thumbnail_url = []
                    for video in videos:
                        vid_id.append(str(video["videoId"]))
                        url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                        video = pafy.new(url)
                        thumbnail_url.append(video.bigthumbhd)
                    videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/HiteshChoudharydotcom",
                                                    limit=50, sort_by="newest")
                    for video in videos:
                        vid_id.append(str(video["videoId"]))
                        url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                        video = pafy.new(url)
                        thumbnail_url.append(video.bigthumbhd)
                    videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/Telusko", limit=50,
                                                    sort_by="newest")
                    for video in videos:
                        vid_id.append(str(video["videoId"]))
                        url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                        video = pafy.new(url)
                        thumbnail_url.append(video.bigthumbhd)
                    videos = scrapetube.get_channel(channel_url="https://www.youtube.com/user/saurabhexponent1",
                                                    limit=50, sort_by="newest")
                    for video in videos:
                        vid_id.append(str(video["videoId"]))
                        url = "https://www.youtube.com/watch?v=" + str(video["videoId"])
                        video = pafy.new(url)
                        thumbnail_url.append(video.bigthumbhd)

                    # Credentials for youtube api
                    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
                    api_service_name = "youtube"
                    api_version = "v3"
                    DEVELOPER_KEY = "AIzaSyC1nYmW4R4FkrOSQZliOPcKANTHEk47Ric"
                    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
                    for vidId in vid_id:
                        req = youtube.commentThreads().list(part="snippet, replies", order="time", maxResults=100, textFormat="plainText", videoId=vidId)
                        response = req.execute()
                        full = pd.json_normalize(response, record_path=['items'])
                        while response:
                            if 'nextPageToken' in response:
                                response = youtube.commentThreads().list(part="snippet", maxResults=100, textFormat='plainText', order='time',videoId=vidId, pageToken=response['nextPageToken']).execute()
                                df2 = pd.json_normalize(response, record_path=['items'])
                                full = full.append(df2)

                            else:
                                break
                        full = full[["id", "snippet.topLevelComment.snippet.textDisplay","snippet.topLevelComment.snippet.authorDisplayName","snippet.topLevelComment.snippet.likeCount", "snippet.totalReplyCount"]]
                        full.columns = ["id", "comment_text", "commenter_name", "likes_count", "replies_count"]
                        # Fetching replies to comments
                        try:
                            list_id = list(full.loc[full["replies_count"] > 0]["id"])
                            for parentId in list_id:
                                req = youtube.comments().list(part="snippet", maxResults=100, parentId=parentId,
                                                                  textFormat="plainText")
                                response = req.execute()
                                replies = pd.json_normalize(response, record_path=['items'])
                                replies = replies[["id", "snippet.textDisplay", "snippet.authorDisplayName", "snippet.likeCount"]]
                                replies.columns = ["id", "comment_text", "commenter_name", "likes_count"]
                                full = pd.concat([full, replies], sort=False, axis=0)
                        except:
                            full = full
                        mongo_vid_id = [vidId] * full.shape[0]
                        full["video_id"] = mongo_vid_id
                        datab.comments.insert_many(full.to_dict('records'))
                    mongo_list = []
                    for image in thumbnail_url:
                        # Getting image in bytes
                        response = requests.get(image)
                        # image encoding
                        encoded_image = base64.b64encode(response.content)
                        mydict = {image: encoded_image}
                        mongo_list.append(mydict)
                        # # image decoding and saving the image
                        # decoded_image= base64.b64decode(encoded_image)
                        # # For reading and saving the image in local system
                        # with open("imageToSave.png", "wb") as fh:
                        #     fh.write(decoded_image)
                    datab.image.insert_many(mongo_list)
                    return render_template('index.html')
                except:
                    pass
            except Exception as e:
                return e

    except Exception as e:
        return e


#For returning the comments for a particular video
@app.route('/video_url', methods=['POST', 'GET'])  # route to show the youtube video comments
@cross_origin()
def video_com():
    if request.method == 'POST':
        try:
            # For returning comments for a particular video
            url= request.form["vid_link"]
            mongocred=request.form["mong"]
            client = pymongo.MongoClient(mongocred,tlsCAFile=certifi.where())
            datab = client.youtube
            questions = datab.comments.find({"video_id": url[32:]}, {})
            return render_template('comment.html', questions=questions)
        except Exception as e:

            return e

if __name__ == "__main__":
    app.run(port=5002, debug=True)