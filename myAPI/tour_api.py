import requests as req
import os


def deco(func):
    def wrapper(*args, **kwargs):
        try:
            url, parm = func(*args, **kwargs)
            res = req.get(url, parm)
            data = res.json()
            data = data['response']['body']['items']['item']
            return data
        except Exception as e:
            print('=' * 100)
            print(e)
            print('=' * 100)
        return None

    return wrapper


class ktorecruitment:
    """
        한국관광공사_채용정보_현황 - 1.0.0
        [ Base URL: apis.data.go.kr/B551011/ktorecruitment ]
        한국관광공사 홈페이지에서 등록된 채용 정보를 제공합니다.
        이용 허락 범위: 제한 없음

        https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043125
    """

    def __init__(self):
        self.base_url = 'http://apis.data.go.kr/B551011/ktorecruitment'
        self.serviceKey = os.environ['TOUR_API_KEY']

    def getDatament(self, startdt, enddt):
        """
            GET : /getDatament
            한국 관광 공사 채용 정보 조회
            한국관광공사 홈페이지에 등록된 채용정보 목록을 게시일 기준으로 게시글 제목, 게시글 URL, 접수 마감일 등을 조회하는 채용정보 조회 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 발급받은 인증키
            startdt *           string          조회 시작일(등록일 기준)
            enddt *             string          조회 종료일(등록일 기준)
        """
        parm = {
            'startdt': startdt,
            'enddt': enddt,
        }
        url = f'{self.base_url}/getDatament?serviceKey={self.serviceKey}'
        res = req.get(url, parm)
        data = res.json()
        data = data['response']['result']['resultItem']
        return data


class Durunubi:
    """
        한국관광공사_두루누비 정보 서비스_GW - 1.0.0
        [ Base URL: apis.data.go.kr/B551011/Durunubi ]
        걷기, 자전거 등 인간의 힘을 이용한 레저여행에 대해 코스정보를 중심으로 주변 관광정보를 종합 제공하는 통합여행정보 서비스인 '두루누비'의 길 정보와 코스 정보를 제공합니다. #걷기, #걷기여행, #걷기여행길, #코리아둘레길, #해파랑길, #서해랑길, #남파랑길, #DMZ 평화의길
        이용 허락 범위: 제한 없음

        https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15101974
    """

    def __init__(self, MobileOS='ETC', MobileApp='GAYOU', _type='json'):
        self.base_url = 'http://apis.data.go.kr/B551011/Durunubi'
        self.parm = {
            'MobileOS': MobileOS,
            'MobileApp': MobileApp,
            '_type': _type,
        }
        self.serviceKey = os.environ['TOUR_API_KEY']

    @deco
    def courseList(self, numOfRows=10, pageNo=1, crsKorNm='', routeIdx='', crsLevel='', brdDiv=''):
        """
            GET : /courseList
            코스 목록 정보 조회
            코스 목록 정보를 조회하는 기능입니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          인증키(서비스키)
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            numOfRows           string          한페이지결과수
            pageNo              string          페이지번호
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            crsKorNm            string          코스명
            routeIdx            string          길 고유번호
            crsLevel            string          난이도(하:1, 중:2, 상:3)
            brdDiv              string          걷기/자전거 구분(DNBW=자전거 길, DNWW=걷기 길)
        """
        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'crsKorNm': crsKorNm,
            'routeIdx': routeIdx,
            'crsLevel': crsLevel,
            'brdDiv': brdDiv,
        })
        url = f'{self.base_url}/courseList?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def routeList(self, numOfRows=10, pageNo=1, themeNm='', brdDiv=''):
        """
            GET : /routeList
            길 목록 정보 조회
            길 목록 정보를 조회하는 기능입니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          인증키(서비스키)
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            numOfRows           string          한페이지결과수
            pageNo              string          페이지번호
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            themeNm             string          길 명
            brdDiv              string          걷기/자전거 구분(DNBW=자전거 길, DNWW=걷기 길)
        """
        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'themeNm': themeNm,
            'brdDiv': brdDiv,
        })
        url = f'{self.base_url}/routeList?serviceKey={self.serviceKey}'
        return url, self.parm


class ForFriTourService:
    """
        한국관광공사_외래객 친화 관광정보 GW - 1.0.0
        [ Base URL: apis.data.go.kr/B551011/ForFriTourService ]
        한국관광공사가 수집한 동남아시아, 중동 관광객을 대상 주요 관광지 주변에 식당, 기도실 등 편의시설 정보를 제공합니다.
        이용 허락 범위: 제한 없음
        https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15111159
    """

    def __int__(self, MobileOS='ETC', MobileApp='GAYOU', _type='json'):
        self.base_url = 'http://apis.data.go.kr/B551011/ForFriTourService'
        self.parm = {
            'MobileOS': MobileOS,
            'MobileApp': MobileApp,
            '_type': _type,
        }
        self.serviceKey = os.environ['TOUR_API_KEY']

    @deco
    def locationBasedList(self, mapX, mapY, radius, numOfRows=10, pageNo=1, arrange='', contentTypeId='',
                          modifiedtime=''):
        """
            GET : /locationBasedList
            위치 기반 관광 정보 조회
            내주변 좌표를 기반으로 외래객 친화 관광정보 목록을 조회하는 기능입니다. 파라미터에 따라 제목순, 수정일순(최신순), 등록일순, 거리순 정렬검색을 제공합니다.(이미지 : 공공누리1,3유형만 제공만)

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 받은 인증키
            MobileOS *          string          IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC
            MobileApp *         string          서비스명=어플명
            mapX *              string          GPS X좌표(WGS84 경도 좌표)
            mapY *              string          GPS Y좌표(WGS84 위도 좌표)
            radius *            string          거리 반경(단위:m) , Max값 20000m=20Km
            numOfRows           number          한 페이지 결과 수
            pageNo              number          현재 페이지 번호
            arrange             string          정렬구분(A=제목순, C=수정일순, D=생성일순, E=거리순) 대표이미지가반드시있는정렬 (O=제목순, Q=수정일순, R=생성일순,S=거리순)
            contentTypeId       string          관광타입(1145:음식 , 1146:기도실) ID
            modifiedtime        string          수정일(형식 :YYYYMMDD)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
        """
        self.parm.update({
            'mapX': mapX,
            'mapY': mapY,
            'radius': radius,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'arrange': arrange,
            'contentTypeId': contentTypeId,
            'modifiedtime': modifiedtime,
        })
        url = f'{self.base_url}/locationBasedList?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def searchKeyword(self, keyword, numOfRows=10, pageNo=1, arrange='', contentTypeId='', areaCode='', sigunguCode=''):
        """
            GET : /searchKeyword
            키워드 검색 조회
            키워드로 검색을 하여 타입별 또는 전체 목록을 조회하는 기능입니다. 파라미터에 따라 제목순, 수정일순(최신순), 등록일순 정렬검색을 제공합니다.(이미지 : 공공누리1,3유형만 제공만)

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 받은 인증키
            numOfRows           number          한 페이지 결과 수
            pageNo              number          현재 페이지 번호
            MobileOS *          string          IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC
            MobileApp *         string          서비스명=어플명
            arrange             string          정렬구분(A=제목순, C=수정일순, D=생성일순)대표이미지가반드시있는정렬(O=제목순, Q=수정일순, R=생성일순)
            contentTypeId       string          관광타입(1145:음식 , 1146:기도실) ID
            keyword *           string          검색 요청할 키워드
            areaCode            string          지역코드
            sigunguCode         string          시군구코드
            _type *             string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
        """
        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'arrange': arrange,
            'contentTypeId': contentTypeId,
            'keyword': keyword,
            'areaCode': areaCode,
            'sigunguCode': sigunguCode,
        })
        url = f'{self.base_url}/searchKeyword?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def detailCommon(self, contentId, contentTypeId='', numOfRows=10, pageNo=1):
        """
            GET : /detailCommon
            공통 정보 조회
            타입별(음식,기도실) 공통정보(제목, 주소, 좌표 등)를 조회하는 기능입니다.(이미지 : 공공누리1,3유형만 제공만)

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 받은 인증키
            MobileOS *          string          OS 구분
            MobileApp *         string          서비스명
            contentId *         string          콘텐츠ID
            contentTypeId       string          관광타입(1145:음식 , 1146:기도실) ID
            numOfRows           number          한 페이지 결과수
            pageNo              number          현재 페이지 번호
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
        """
        self.parm.update({
            'contentId ': contentId,
            'contentTypeId': contentTypeId,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
        })
        url = f'{self.base_url}/detailCommon?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def detailImage(self, contentId, numOfRows=10, pageNo=1, imageYN='', subImageYN=''):
        """
            GET : /detailImage
            이미지 정보 조회
            각 관광타입(음식,기도실)에 해당하는 이미지url 목록을 조회하는 기능입니다.(이미지 : 공공누리1,3유형만 제공만)

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 받은 인증키
            MobileOS *          string          OS 구분
            MobileApp *         string          서비스명
            contentId *         string          콘텐츠ID
            numOfRows           number          한 페이지 결과수
            pageNo              number          현재 페이지 번호
            imageYN             string          Y=이미지, N=SubImage(음식:메뉴이미지)
            subImageYN          string          Y=원본,썸네일이미지조회,공공누리 저작권유형정보조회 N=Null
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
        """
        self.parm.update({
            'contentId': contentId,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'imageYN': imageYN,
            'subImageYN': subImageYN,
        })
        url = f'{self.base_url}/detailImage?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def areaCode(self, numOfRows=10, pageNo=1, areaCode=''):
        """
            GET : /areaCode
            지역 코드 조회
            지역코드, 시군구코드 목록을 조회하는 기능입니다. 지역기반 외래객 친화 관광정보 및 키워드 검색을 통해 지역별로 목록을 보여줄 경우, 지역코드를 이용하여 지역명을 매칭하기 위한 기능입니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한 페이지 결과 수
            pageNo              number          현재 페이지 번호
            MobileOS *          string          IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC
            MobileApp *         string          서비스명=어플명
            areaCode            string          지역코드, 시군구코드
            serviceKey *        string          인증키(서비스키)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
        """
        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'areaCode': areaCode,
        })
        url = f'{self.base_url}/areaCode?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def areaBasedList(self, numOfRows=10, pageNo=1, arrange='', contentTypeId='', areaCode='', sigunguCode='',
                      modifiedtime=''):
        """
            GET : /areaBasedList
            지역 기반 관광 정보 조회
            지역 및 시군구를 기반으로 외래객 친화 관광정보 목록입니다. 파라미터에 따라 제목순, 수정일순(최신순)등록일순 정렬검색을 제공합니다.(이미지 : 공공누리1,3유형만 제공만)

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 받은 인증키
            numOfRows           number          한 페이지 결과 수
            pageNo              number          현재 페이지 번호
            MobileOS *          string          IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC
            MobileApp *         string          서비스명=어플명
            arrange             string          정렬구분(A=제목순, C=수정일순, D=생성일순)대표이미지가반드시있는정렬(O=제목순, Q=수정일순, R=생성일순)
            contentTypeId       string          관광타입(1145:음식 , 1146:기도실) ID
            areaCode            string          지역코드
            sigunguCode         string          시군구코드
            modifiedtime        string          수정일(형식 :YYYYMMDD)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
        """

        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'arrange': arrange,
            'contentTypeId': contentTypeId,
            'areaCode': areaCode,
            'sigunguCode': sigunguCode,
            'modifiedtime': modifiedtime,
        })
        url = f'{self.base_url}/areaBasedList?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def detailIntro(self, contentId, contentTypeId='', numOfRows=10, pageNo=1):
        """
            GET : /detailIntro
            소개 정보 조회
            타입별(음식,기도실) 소개정보(할랄메뉴, 운영시간, 코란 등)를 조회하는 기능입니다. 각 타입마다 응답 항목이 다르게 제공됩니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 받은 인증키
            MobileOS *          string          OS 구분
            MobileApp *         string          서비스명
            contentId *         string          콘텐츠ID
            contentTypeId       string          관광타입(1145:음식 , 1146:기도실) ID
            numOfRows           number          한 페이지 결과수
            pageNo              number          현재 페이지 번호
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
        """

        self.parm.update({
            'contentId': contentId,
            'contentTypeId': contentTypeId,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
        })
        url = f'{self.base_url}/detailIntro?serviceKey={self.serviceKey}'

        return url, self.parm


class tursmService:
    """
        한국관광공사_관광인_채용정보_서비스_GW - 1.0.0
        [ Base URL: apis.data.go.kr/B551011/tursmService ]
        한국관광공사 관광전문인력포털 관광인에서 보유하고 있는 채용제목, 모집직종, 직무내용, 우대조건 등 채용정보를 제공합니다.
        이용 허락 범위: 제한 없음
        https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15125070
    """

    def __int__(self, MobileOS='ETC', MobileApp='GAYOU', _type='json'):
        self.base_url = 'http://apis.data.go.kr/B551011/tursmService'
        self.parm = {
            'MobileOS': MobileOS,
            'MobileApp': MobileApp,
            '_type': _type,
        }
        self.serviceKey = os.environ['TOUR_API_KEY']

    @deco
    def empmnInfoList(self, pageNo=1, numOfRows=10, regnCd='', signguCd='', wrkpAdresText='', empmnTitle='',
                      rcritJssfcCd='', crrDivCd='', acdmcrCd='', salStleCd='', minWageAmt='', maxWageAmt='',
                      eplmtStleCd='', minRegDt='', maxRegDt='', arrange='', dspsnEmpmnHopeCd=''):
        """
            GET : /empmnInfoList
            채용 정보 목록 조회
            채용정보 목록을 조회하능 기능입니다. 채용정보 목록을 조회해 채용정보글의 기본 정보를 획득합니다. 채용정보 번호를 이용해 상세 정보 검색이 가능합니다. 검색 조건들은 AND 조건으로 추가됩니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 받은 인증키
            pageNo              number          페이지번호
            numOfRows           number          한 페이지 결과 수
            MobileOS *          string          IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC
            MobileApp *         string          서비스명=어플명
            regnCd              string          지역코드 검색조건 (코드조회(codeType=AREA)에서 확인가능)
            signguCd            string          지역코드에 해당하는 시군구코드 검색조건 (코드조회(codeType=AREA)에서 확인가능)
            wrkpAdresText       string          근무지 주소 텍스트로 검색
            empmnTitle          string          채용제목 텍스트로 검색
            rcritJssfcCd        string          모집직종 코드. 검색 조건 (코드조회(codeType=JOB)에서 확인가능) 상위 코드 입력시 해당하는 코드의 하위 코드내용도 검색한다. 반점으로 추가 코드 입력 시 OR 조건으로 추가
            crrDivCd            string          경력구분코드. 중위코드 JC01에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
            acdmcrCd            string          학력코드. 중위코드 JC18에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
            salStleCd           string          급여형태코드. JC06에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
            minWageAmt          string          임금 범위검색 : 최소임금금액. [급여형태코드] 월급(JC0602), 연봉(JC0601)일 시 단위 : 만원, 이외 단위 : 원. 빈값 시 [임금 범위검색: 최대임금금액] 이하로 검색
            maxWageAmt          string          임금 범위검색 : 최대임금금액. [급여형태코드] 월급(JC0602), 연봉(JC0601)일 시 단위 : 만원, 이외 단위 : 원. 빈값 시 [임금 범위검색: 최소임금금액] 이상로 검색
            eplmtStleCd         string          고용형태코드. 중위코드 JC02, JC03에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
            minRegDt            string          등록일 범위검색 : 시작일. 빈값 시 [등록일 범위검색 : 종료일] 이하로 검색
            maxRegDt            string          등록일 범위검색 : 종료일. 빈값 시 [등록일 범위검색 : 시작일] 이상으로 검색
            arrange             string          정렬 구분 (A=제목순, D=등록일순, M=수정일순, S=학력순, G=경력순). 대문자 내림차순 소문자로 입력시 오름차순
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            dspsnEmpmnHopeCd    string          장애인채용희망코드. 중위코드 JC11에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능)
        """
        self.parm.update({
            'pageNo': pageNo,
            'numOfRows': numOfRows,
            'regnCd': regnCd,
            'signguCd': signguCd,
            'wrkpAdresText': wrkpAdresText,
            'empmnTitle': empmnTitle,
            'rcritJssfcCd': rcritJssfcCd,
            'crrDivCd': crrDivCd,
            'acdmcrCd': acdmcrCd,
            'salStleCd': salStleCd,
            'minWageAmt': minWageAmt,
            'maxWageAmt': maxWageAmt,
            'eplmtStleCd': eplmtStleCd,
            'minRegDt': minRegDt,
            'maxRegDt': maxRegDt,
            'arrange': arrange,
            'dspsnEmpmnHopeCd': dspsnEmpmnHopeCd,
        })
        url = f'{self.base_url}/empmnInfoList?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def empmnInfoDetail(self, empmnInfoNo, pageNo=1, numOfRows=10):
        """
            GET : /empmnInfoDetail
            채용 정보 상세 조회
            채용정보의 상세한 정보를 조회하는기능입니다. 목록정보에서 얻은 채용정보번호로 상세정보를 추출합니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한 페이지 결과 수
            pageNo              number          현재 페이지 번호
            MobileOS *          string          IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC
            MobileApp *         string          서비스명=어플명
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            empmnInfoNo *       string          채용정보 번호 (목록에서 조회가능)
            serviceKey *        string          공공데이터포털에서 받은 인증키
        """
        self.parm.update({
            'empmnInfoNo': empmnInfoNo,
            'pageNo': pageNo,
            'numOfRows': numOfRows,
        })
        url = f'{self.base_url}/empmnInfoDetail?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def syncList(self, pageNo=1, numOfRows=10, regnCd='', signguCd='', wrkpAdresText='', empmnTitle='',
                 rcritJssfcCd='', crrDivCd='', acdmcrCd='', salStleCd='', minWageAmt='', maxWageAmt='', eplmtStleCd='',
                 minRegDt='', maxRegDt='', arrange='', minMdfcnDt='', maxMdfcnDt='', showYn='', dspsnEmpmnHopeCd=''):
        """
            GET : /syncList
            동기화 목록 조회
            채용정보 목록을 조회하는 기능입니다. 채용정보 목록을 조회해 채용정보글의 기본 정보를 획득합니다. 채용정보 번호를 이용해 상세 정보 검색이 가능합니다. 채용정보 목록과 다르게 사용여부 상관없이 조회합니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            pageNo              number          페이지번호
            numOfRows           number          한 페이지 결과 수
            MobileOS *          string          IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC
            MobileApp *         string          서비스명=어플명
            regnCd              string          지역코드 검색조건 (코드조회(codeType=AREA)에서 확인가능)
            signguCd            string          지역코드에 해당하는 시군구코드 검색조건 (코드조회(codeType=AREA)에서 확인가능). 지역코드 필수 입력
            wrkpAdresText       string          근무지 주소 텍스트로 검색
            empmnTitle          string          채용제목 텍스트로 검색
            rcritJssfcCd        string          모집직종 코드 검색 조건 (코드조회(codeType=JOB)에서 확인가능) 상위 코드 입력시 해당하는 코드의 하위 코드내용도 검색한다. 반점으로 추가 코드 입력 시 OR 조건으로 추가
            crrDivCd            string          경력구분코드. 중위코드 JC01에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
            acdmcrCd            string          학력코드. 중위코드 JC18에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
            salStleCd           string          급여형태코드. 중위코드 JC06에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
            minWageAmt          string          임금 범위검색 : 최소임금금액. [급여형태코드] 월급(JC0602), 연봉(JC0601)일 시 단위 : 만원, 이외 단위 : 원. 빈값 시 [임금 범위검색: 최대임금금액] 이하로 검색
            maxWageAmt          string          임금 범위검색 : 최대임금금액. [급여형태코드] 월급(JC0602), 연봉(JC0601)일 시 단위 : 만원, 이외 단위 : 원. 빈값 시 [임금 범위검색: 최소임금금액] 이상으로 검색
            eplmtStleCd         string          중위코드 JC02, JC03에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
            minRegDt            string          등록일 범위검색 : 시작일. 빈값 시 [등록일 범위검색 : 종료일] 이하로 검색
            maxRegDt            string          등록일 범위검색 : 종료일. 빈값 시 [등록일 범위검색 : 시작일] 이상으로 검색
            arrange             string          정렬 구분 (A=제목순, D=등록일순, M=수정일순, S=학력순, G=경력순). 대문자 내림차순 소문자로 입력시 오름차순
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            minMdfcnDt          string          수정일 범위검색 : 시작일. 빈값 시 [수정일 범위검색 : 종료일] 이하로 검색
            maxMdfcnDt          string          수정일 범위검색 : 종료일. 빈값 시 [수정일 범위검색 : 시작일] 이상으로 검색
            serviceKey *        string          인증키(서비스키)
            showYn              string          표출여부
            dspsnEmpmnHopeCd    string          장애인채용희망코드. 중위코드 JC11에 해당하는 코드(코드조회(codeType=COMM)에서 확인가능) 반점으로 추가코드 입력 시 OR 조건으로 추가
        """
        self.parm.update({
            'pageNo': pageNo,
            'numOfRows': numOfRows,
            'regnCd': regnCd,
            'signguCd': signguCd,
            'wrkpAdresText': wrkpAdresText,
            'empmnTitle': empmnTitle,
            'rcritJssfcCd': rcritJssfcCd,
            'crrDivCd': crrDivCd,
            'acdmcrCd': acdmcrCd,
            'salStleCd': salStleCd,
            'minWageAmt': minWageAmt,
            'maxWageAmt': maxWageAmt,
            'eplmtStleCd': eplmtStleCd,
            'minRegDt': minRegDt,
            'maxRegDt': maxRegDt,
            'arrange': arrange,
            'minMdfcnDt': minMdfcnDt,
            'maxMdfcnDt': maxMdfcnDt,
            'showYn': showYn,
            'dspsnEmpmnHopeCd': dspsnEmpmnHopeCd,
        })
        url = f'{self.base_url}/syncList?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def code(self, codeType, code='', numOfRows=10, pageNo=1):
        """
            GET : /code
            코드 조회
            지역, 직업명세, 공통코드 목록을 조회하는 기능입니다. 코드를 조회 해 채용정보 목록의 검색조건 및 결과값 매칭에 사용됩니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type *             string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            codeType *          string          코드 검색 조건 (AREA : 지역, JOB : 직업, COMM: 공통)
            code                string          코드에 해당하는 하위코드 조회 (직업코드는 상,중,하위 코드 존재, 그 외 중,하위 코드 존재)
            serviceKey *        string          공공데이터포털에서 받은 인증키
        """
        self.parm.update({
            'codeType': codeType,
            'code': code,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
        })
        url = f'{self.base_url}/code?serviceKey={self.serviceKey}'

        return url, self.parm


class KorService1:
    """
        한국관광공사_국문 관광정보 서비스_GW - 1.0.0
        [ Base URL: apis.data.go.kr/B551011/KorService1 ]
        코드조회 및 관광정보의 통합/상세 검색 및 위치기반,지역기반 등 국내 관광에 대한 전반적인 상세정보를 국문관광정보로 제공한다.
        이용 허락 범위: 제한 없음

        https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15101578
    """

    def __int__(self, MobileOS='ETC', MobileApp='GAYOU', _type='json'):
        self.base_url = 'http://apis.data.go.kr/B551011/tursmService'
        self.parm = {
            'MobileOS': MobileOS,
            'MobileApp': MobileApp,
            '_type': _type,
        }
        self.serviceKey = os.environ['TOUR_API_KEY']

    @deco
    def locationBasedList1(self, mapX, mapY, radius, numOfRows=10, pageNo=1, listYN='', arrange='', contentTypeId='',
                           modifiedtime=''):
        """
            GET : /courseList
            위치 기반 관광 정보 조회
            위치기반 관광정보파라미터 타입에 따라서 제목순,수정일순,등록일순 정렬검색목록을 조회하는 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            listYN              string          목록구분(Y=목록, N=개수)
            arrange             string          정렬구분 (A=제목순, C=수정일순, D=생성일순) 대표이미지가반드시있는정렬(O=제목순, Q=수정일순, R=생성일순)
            mapX *              string          GPS X좌표(WGS84 경도좌표)
            mapY *              string          GPS Y좌표(WGS84 위도좌표)
            radius *            string          거리반경(단위:m) , Max값 20000m=20Km
            contentTypeId       string          관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 25:여행코스, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID
            modifiedtime        string          수정일(형식 :YYYYMMDD)
            serviceKey *        string          인증키(서비스키)
        """
        self.parm.update({
            'mapX': mapX,
            'mapY': mapY,
            'radius': radius,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'listYN': listYN,
            'arrange': arrange,
            'contentTypeId': contentTypeId,
            'modifiedtime': modifiedtime,
        })
        url = f'{self.base_url}/locationBasedList1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def searchKeyword1(self, keyword, numOfRows=10, pageNo=1, listYN='', arrange='', contentTypeId='', areaCode='',
                       sigunguCode='', cat1='', cat2='', cat3=''):
        """
            GET : /searchKeyword1
            키워드 검색 조회
            키워드로 검색을하며 전체별 타입정보별 목록을 조회한다

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            listYN              string          목록구분(Y=목록, N=개수)
            arrange             string          정렬구분 (A=제목순, C=수정일순, D=생성일순) 대표이미지가반드시있는정렬(O=제목순, Q=수정일순, R=생성일순)
            keyword *           string          검색요청할키워드 : (국문=인코딩필요) 샘플 - 강원
            contentTypeId       string          관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 25:여행코스, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID
            areaCode            string          지역코드(지역코드조회 참고)
            sigunguCode         string          시군구코드(지역코드조회 참고)
            cat1                string          대분류(서비스분류코드조회 참고)
            cat2                string          중분류(서비스분류코드조회 참고)
            cat3                string          소분류(서비스분류코드조회 참고)
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'keyword': keyword,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'listYN': listYN,
            'arrange': arrange,
            'contentTypeId': contentTypeId,
            'areaCode': areaCode,
            'sigunguCode': sigunguCode,
            'cat1': cat1,
            'cat2': cat2,
            'cat3': cat3,
        })
        url = f'{self.base_url}/searchKeyword1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def searchFestival1(self, eventStartDate, numOfRows=10, pageNo=1, listYN='', arrange='', eventEndDate='',
                        areaCode='', sigunguCode='', modifiedtime=''):
        """
            GET : /searchFestival1
            행사 정보 조회
            행사정보목록을 조회한다. 컨텐츠 타입이 ‘행사’일 경우에만 유효하다

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            listYN              string          목록구분(Y=목록, N=개수)
            arrange             string          정렬구분 (A=제목순, C=수정일순, D=생성일순) 대표이미지가반드시있는정렬(O=제목순, Q=수정일순, R=생성일순)
            eventStartDate *    string          행사시작일(형식 :YYYYMMDD)
            eventEndDate        string          행사종료일(형식 :YYYYMMDD)
            areaCode            string          지역코드(지역코드조회 참고)
            sigunguCode         string          시군구코드(지역코드조회 참고)
            modifiedtime        string          수정일(형식 :YYYYMMDD)
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'eventStartDate': eventStartDate,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'listYN': listYN,
            'arrange': arrange,
            'eventEndDate': eventEndDate,
            'areaCode': areaCode,
            'sigunguCode': sigunguCode,
            'modifiedtime': modifiedtime,
        })
        url = f'{self.base_url}/searchFestival1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def searchStay1(self, numOfRows=10, pageNo=1, listYN='', arrange='', areaCode='', sigunguCode='', modifiedtime=''):
        """
            GET : /searchStay1
            숙박 정보 조회
            숙박정보 검색목록을 조회한다. 컨텐츠 타입이 ‘숙박’일 경우에만 유효하다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            listYN              string          목록구분(Y=목록, N=개수)
            arrange             string          정렬구분 (A=제목순, C=수정일순, D=생성일순) 대표이미지가반드시있는정렬(O=제목순, Q=수정일순, R=생성일순)
            areaCode            string          지역코드(지역코드조회 참고)
            sigunguCode         string          시군구코드(지역코드조회 참고)
            modifiedtime        string          수정일(형식 :YYYYMMDD)
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'listYN': listYN,
            'arrange': arrange,
            'areaCode': areaCode,
            'sigunguCode': sigunguCode,
            'modifiedtime': modifiedtime,
        })
        url = f'{self.base_url}/searchStay1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def detailCommon1(self, contentId, contentTypeId='', defaultYN='', firstImageYN='', areacodeYN='', catcodeYN='',
                      addrinfoYN='', mapinfoYN='', overviewYN='', numOfRows=10, pageNo=1):
        """
            GET : /detailCommon1s
            공통 정보 조회
            타입별공통 정보기본정보,약도이미지,대표이미지,분류정보,지역정보,주소정보,좌표정보,개요정보,길안내정보,이미지정보,연계관광정보목록을 조회하는 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            contentId *         string          콘텐츠ID
            contentTypeId       string          관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 25:여행코스, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID
            defaultYN           string          기본정보조회여부( Y,N )
            firstImageYN        string          원본, 썸네일대표 이미지, 이미지 공공누리유형정보 조회여부( Y,N )
            areacodeYN          string          지역코드, 시군구코드조회여부( Y,N )
            catcodeYN           string          대,중,소분류코드조회여부( Y,N )
            addrinfoYN          string          주소, 상세주소조회여부( Y,N )
            mapinfoYN           string          좌표X, Y 조회여부( Y,N )
            overviewYN          string          콘텐츠개요조회여부( Y,N )
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'contentId': contentId,
            'contentTypeId': contentTypeId,
            'defaultYN': defaultYN,
            'firstImageYN': firstImageYN,
            'areacodeYN': areacodeYN,
            'catcodeYN': catcodeYN,
            'addrinfoYN': addrinfoYN,
            'mapinfoYN': mapinfoYN,
            'overviewYN': overviewYN,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
        })
        url = f'{self.base_url}/detailCommon1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def detailIntro1(self, contentId, contentTypeId, numOfRows=10, pageNo=1):
        """
            GET : /detailIntro1
            소개 정보 조회
            상세소개 쉬는날, 개장기간 등 내역을 조회하는 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            contentId *         string          콘텐츠ID
            contentTypeId *     string          관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 25:여행코스, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'contentId': contentId,
            'contentTypeId': contentTypeId,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
        })
        url = f'{self.base_url}/detailIntro1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def detailInfo1(self, contentId, contentTypeId, numOfRows=10, pageNo=1):
        """
            GET : /detailInfo1
            반복 정보 조회
            추가 관광정보 상세내역을 조회한다. 상세반복정보를 안내URL의 국문관광정보 상세 매뉴얼 문서를 참고하시기 바랍니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            contentId *         string          콘텐츠ID
            contentTypeId *     string          관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'contentId': contentId,
            'contentTypeId': contentTypeId,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
        })
        url = f'{self.base_url}/detailInfo1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def detailImage1(self, contentId, imageYN='', subImageYN='', numOfRows=10, pageNo=1):
        """
            GET : /detailImage1
            이미지 정보 조회
            관광정보에 매핑되는 서브이미지목록 및 이미지 자작권 공공누리유형을 조회하는 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            contentId *         string          콘텐츠ID
            imageYN             string          이미지조회1 : Y=콘텐츠이미지조회 N=”음식점”타입의음식메뉴이미지
            subImageYN          string          이미지조회2 : Y=원본,썸네일이미지조회,공공누리 저작권유형정보조회 N=Null
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'contentId': contentId,
            'imageYN': imageYN,
            'subImageYN': subImageYN,
            'numOfRows': numOfRows,
            'pageNo': pageNo,
        })
        url = f'{self.base_url}/detailImage1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def areaBasedSyncList1(self, numOfRows='', pageNo='', showflag='', modifiedtime='', listYN='', arrange='',
                           contentTypeId='', areaCode='', sigunguCode='', cat1='', cat2='', cat3=''):
        """
            GET : /areaBasedSyncList1
            관광 정보 동기화 목록 조회
            지역기반 관광정보파라미터 타입에 따라서 제목순,수정일순,등록일순 정렬검색목록을 조회하는 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            serviceKey *        string          인증키(서비스키)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            showflag            string          컨텐츠표출여부(1=표출, 0=비표출)
            modifiedtime        string          컨텐츠변경일자 (수정년도,수정년월,수정년월일 입력,YYYYMMDD)
            listYN              string          목록 구분 (Y=목록, N=개수)
            arrange             string          정렬 구분 (A=제목순, C=수정일순, D=생성일순) 대표이미지가 반드시 있는 정렬 (O=제목순, Q=수정일순, R=생성일순)
            contentTypeId       string          관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 25:여행코스, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID
            areaCode            string          지역코드(지역코드조회 참고)
            sigunguCode         string          시군구코드(지역코드조회 참고)
            cat1                string          대분류 코드(서비스분류코드조회 참고)
            cat2                string          중분류 코드(서비스분류코드조회 참고)
            cat3                string          소분류 코드(서비스분류코드조회 참고)
        """

        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'showflag': showflag,
            'modifiedtime': modifiedtime,
            'listYN': listYN,
            'arrange': arrange,
            'contentTypeId': contentTypeId,
            'areaCode': areaCode,
            'sigunguCode': sigunguCode,
            'cat1': cat1,
            'cat2': cat2,
            'cat3': cat3,
        })
        url = f'{self.base_url}/areaBasedSyncList1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def areaCode1(self, numOfRows='', pageNo='', areaCode=''):
        """
            GET : /areaCode1
            지역 코드 조회
            지역코드목록을 지역,시군구,읍면동 코드목록을 조회하는 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            areaCode            string          지역코드
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'areaCode': areaCode,
        })
        url = f'{self.base_url}/areaCode1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def detailPetTour1(self, pageNo='', numOfRows='', contentId=''):
        """
            GET : /detailPetTour1
            반려 동물 동반 여행 정보
            타입별 반려동물 동반 여행 정보를 조회하는 기능입니다.

            Parameters
            Name                type            Description
            ----------------------------------------------
            serviceKey *        string          공공데이터포털에서 받은 인증키
            pageNo              number          페이지번호
            numOfRows           number          한 페이지 결과 수
            MobileOS *          string          OS 구분(IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC)
            MobileApp *         string          서비스명
            contentId           string          콘텐츠ID(옵션,미기입시 전체목록조회)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
        """

        self.parm.update({
            'pageNo': pageNo,
            'numOfRows': numOfRows,
            'contentId': contentId,
        })
        url = f'{self.base_url}/detailPetTour1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def categoryCode1(self, numOfRows='', pageNo='', contentTypeId='', cat1='', cat2='', cat3=''):
        """
            GET : /categoryCode1
            서비스 분류 코드 조회
            서비스 분류 코드 목록을 대,중,소분류로 조회하는 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           string          한페이지결과수
            pageNo              string          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            contentTypeId       string          관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 25:여행코스, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID
            cat1                string          대분류코드
            cat2                string          중분류코드
            cat3                string          소분류코드
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'contentTypeId': contentTypeId,
            'cat1': cat1,
            'cat2': cat2,
            'cat3': cat3,
        })
        url = f'{self.base_url}/categoryCode1?serviceKey={self.serviceKey}'

        return url, self.parm

    @deco
    def areaBasedList1(self, numOfRows='', pageNo='', listYN='', arrange='', contentTypeId='', areaCode='',
                       sigunguCode='', cat1='', cat2='', cat3='', modifiedtime=''):
        """
            GET : /areaBasedList1
            지역 기반 관광 정보 조회
            지역기반 관광정보파라미터 타입에 따라서 제목순,수정일순,등록일순 정렬검색목록을 조회하는 기능

            Parameters
            Name                type            Description
            ----------------------------------------------
            numOfRows           number          한페이지결과수
            pageNo              number          페이지번호
            MobileOS *          string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
            MobileApp *         string          서비스명(어플명)
            _type               string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
            listYN              string          목록구분(Y=목록, N=개수)
            arrange             string          정렬구분 (A=제목순, C=수정일순, D=생성일순) 대표이미지가반드시있는정렬(O=제목순, Q=수정일순, R=생성일순)
            contentTypeId       string          관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 25:여행코스, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID
            areaCode            string          지역코드(지역코드조회 참고)
            sigunguCode         string          시군구코드(지역코드조회 참고)
            cat1                string          대분류(서비스분류코드조회 참고)
            cat2                string          중분류(서비스분류코드조회 참고)
            cat3                string          소분류(서비스분류코드조회 참고)
            modifiedtime        string          수정일(형식 :YYYYMMDD)
            serviceKey *        string          인증키(서비스키)
        """

        self.parm.update({
            'numOfRows': numOfRows,
            'pageNo': pageNo,
            'listYN': listYN,
            'arrange': arrange,
            'contentTypeId': contentTypeId,
            'areaCode': areaCode,
            'sigunguCode': sigunguCode,
            'cat1': cat1,
            'cat2': cat2,
            'cat3': cat3,
            'modifiedtime': modifiedtime,
        })
        url = f'{self.base_url}/areaBasedList1?serviceKey={self.serviceKey}'

        return url, self.parm
