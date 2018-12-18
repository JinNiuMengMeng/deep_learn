import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}


def province():  # 省
    province_list = []
    constant = requests.get(url=url, headers=headers)
    con = constant.content.decode(encoding="GB18030")
    soup = BeautifulSoup(con, 'html.parser')
    href = soup.select("a")[0:-1]
    for i in href:
        province_dict = {
            "name": i.text,
            "code": i["href"][0:2],
            "href": url + i["href"],
            "childens": ""
        }
        province_list.append(province_dict)
    return province_list


def province_city(province_city_url):  # 市
    province_city_list = []
    constant = requests.get(url=province_city_url, headers=headers)
    con = constant.content.decode(encoding="GB18030")
    soup = BeautifulSoup(con, 'html.parser')
    href_name = soup.select("tr[class=citytr] td")
    for i in href_name:
        if (href_name.index(i) + 1) % 2 == 0:
            name = i.a.text
        else:
            code = i.a.text
            href = url + i.a["href"]
        if (href_name.index(i) + 1) % 2 == 0:
            province_dict = {
                "name": name,
                "code": code,
                "href": href,
                "childens": ""
            }
            province_city_list.append(province_dict)
    return province_city_list


def province_city_county(province_city_county_url, name):  # 区/县
    province_city_county_list = []
    constant = requests.get(url=province_city_county_url, headers=headers)
    con = constant.content.decode(encoding="GB18030")
    soup = BeautifulSoup(con, 'html.parser')
    href_name = soup.select("tr[class=countytr] td")
    for i in href_name:
        if (href_name.index(i) + 1) % 2 != 0:
            if i.a is None:
                code = i.text
                href = ""
            else:
                code = i.a.text
                href = url + code[0:2] + "/" + i.a["href"]
        else:
            if i.a is None:
                name = i.text
            else:
                name = i.a.text
        if (href_name.index(i) + 1) % 2 == 0:
            province_dict = {
                "name": name,
                "code": code,
                "href": href,
                "childens": ""
            }
            province_city_county_list.append(province_dict)
    return province_city_county_list, name


def province_city_county_street(province_city_county_street_url):  # 街道
    province_city_county_street_list = []
    constant = requests.get(url=province_city_county_street_url, headers=headers)
    con = constant.content.decode(encoding="GB18030")
    soup = BeautifulSoup(con, 'html.parser')
    href_name = soup.select("tr[class=towntr] td")
    for i in href_name:
        if (href_name.index(i) + 1) % 2 != 0:
            code = i.a.text
            href = url + code[0:2] + "/" + code[2:4] + "/" + i.a["href"]
        else:
            name = i.a.text
        if (href_name.index(i) + 1) % 2 == 0:
            province_dict = {
                "name": name,
                "code": code,
                "href": href,
                "childens": ""
            }
            province_city_county_street_list.append(province_dict)
    return province_city_county_street_list


def province_city_county_street_committee(province_city_county_street_committee_url):  # 居委会
    province_city_county_street_committee_list = []
    constant = requests.get(url=province_city_county_street_committee_url, headers=headers)
    con = constant.content.decode(encoding="GB18030")
    soup = BeautifulSoup(con, 'html.parser')
    href_name = soup.select("tr[class=villagetr] td")
    for i in href_name:
        if (href_name.index(i) + 1) % 3 == 0:
            name = i.text
            province_dict = {
                "name": name,
                "code": code,
                "city_code": city_code
            }
            province_city_county_street_committee_list.append(province_dict)
        else:
            if (href_name.index(i) + 1) % 2 == 0:
                city_code = i.text
            else:
                code = i.text
    return province_city_county_street_committee_list


if __name__ == "__main__":
    results = []
    pool = Pool(20)

    province_dict = province()  # 获取省

    for i in province_dict:  # 获取市
        if i["name"] == "内蒙古自治区":
            i["childens"] = province_city(i.get("href"))
            for j in i["childens"]:  # 获取 区/县
                result = pool.apply_async(func=province_city_county, args=(j["href"], j["name"]))
                results.append(result)

            for result in results:
                name = result.get()[-1]
                for j in i["childens"]:
                    if name == j["name"]:
                        j["childens"] = result.get()[0]
            print(i["childens"])
        #         j["childens"] = province_city_county(j["href"])
        #
        #         for m in j["childens"]:  # 获取街道
        #             if len(m["href"]) != 0:
        #                 m["childens"] = province_city_county_street(m["href"])
        #
        #             for n in m["childens"]:   # 获取居委会
        #                 n["childens"] = province_city_county_street_committee(n["href"])
        #
        # print(province_dict)
    pool.close()
    pool.join()
