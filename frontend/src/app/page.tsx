'use client'
import { deleteGroupsAPI, getConfigsAPI, getGroupsAPI, getTasksAPI, patchGroupsAPI, patchPostsAPI, patchPromptsAPI, patchRequestsAPI, postConfigsAPI, postGroupsAPI, postPostsAPI, postPromptsAPI, postRequestsAPI, putConfigsAPI } from "@/api/api"
import { FrameBox } from "./component/atomos/atomos";
import Providers from "./component/hooks/useProviders"
import useAppFrame from "./component/hooks/useAppFrame";

const Page = () => {
  const [AppBar,  SideMenu] = useAppFrame({})

  return (<Providers>
    <FrameBox height={"100%"} direction={"column"}>
      <AppBar/>
      <FrameBox height={"100%"} direction={"row"}>
        <SideMenu/>
      </FrameBox>
    </FrameBox>
  </Providers>)
}
export default Page



const getConfigs    = async () => {
  const res = await getConfigsAPI   ()
  console.log(res)
}
const putConfigs    = async () => {
  const res = await putConfigsAPI   ({request:updateConfigsData})
  console.log(res)
}

const postConfigs   = async () => {
  const res = await postConfigsAPI  ({request:altrConstantsData})
  console.log(res)
}

const getGroups     = async () => {
  const res = await getGroupsAPI    ()
  console.log(res)
}
const postGroups    = async () => {
  const res = await postGroupsAPI   ({request:postGroupData})
  console.log(res)
}

const patchGroups   = async () => {
  const res = await patchGroupsAPI  ({parameter:"8", request:patchGroupData})
  console.log(res)
}

const deleteGroups  = async () => {
  const res = await deleteGroupsAPI ({parameter:"8"})
  console.log(res)
}

const getTasks      = async () => {
  const res = await getTasksAPI     ({parameter:"34"})
  console.log(res)
}

const postPosts     = async () => {
  const res = await postPostsAPI    ({ request: postPostData})
  console.log(res)
}
const patchPosts    = async () => {
  const res = await patchPostsAPI   ({parameter:"1", request: patchPostData})
  console.log(res)
}

const postPrompts   = async () => {
  const res = await postPromptsAPI  ({request: postPrmptData})
  console.log(res)
}
const patchPrompts  = async () => {
  const res = await patchPromptsAPI ({parameter:"1", request: patchPrmptData})
  console.log(res)
}

const postRequests  = async () => {
  const res = await postRequestsAPI ({ request: postReqData })
  console.log(res)
}
const patchRequests = async () => {
  const res = await patchRequestsAPI({parameter:"0", request:patchReqData})
  console.log(res)
}


interface RequestConfigs {
  weights: WeightsInfo
  phrases: PhrasesInfo
}

interface WeightsInfo {
  model:      number[]
  theme:      number[]
  weathers:   number[]
  periods:    number[]
  angles:     number[]
  directions: number[]
  focuses:    number[]
}
interface PhrasesInfo {
  header:        string
  footer:        string
  negative:      string
  request_order: string
  playing_order: string
  posting_desc:  string
  content_desc:  string
}

interface RequestConstants {
  create: ConstantsInfo[]
  update: ConstantsInfo[]
  delete: ConstantsInfo[]
}

interface ConstantsInfo {
  id?:      number
  category: string
  is_lewd:  boolean
  name:     string
  value:    string
}

interface RequestGroup {
  name: string
}

interface RequestPosts {
  task_id:         number
  story:           string
  title_JP:        string
  title_EN:        string
  title_symbol:    string
  picture_count:   string
  wallpaper_count: string
  picture_URL:     string
  wallpaper_URL:   string
  notes:           string[]
}

interface RequestPrompts {
  task_id   : number
  HEADER    : string
  basis     : string
  faces     : string
  hairs     : string
  figures   : string
  location  : string
  outfits   : string
  equips    : string
  emotes    : string
  fluids    : string
  upper     : string
  lower     : string
  actions   : string
  posing    : string
  additional: string
  FOOTER    : string
}

interface RequestRequests {
  basis   : {
    task_id        : number
    model          : number
    thickness      : number
    theme          : number
    species        : string
    species_details: string
    traits         : string
    traits_details : string
  }
  location: {
    task_id          : number
    weathers         : number
    periods          : number
    times            : number
    locations_details: string
  }
  outfits : {
    task_id        : number
    jobs           : string
    jobs_details   : string
    outfits_details: string
    equips_details : string
  }
  hairs   : {
    task_id    : number
    size       : number
    hair_style : string
    bangs_style: string
  }
  faces   : {
    task_id    : number
    looks      : number
    eyes       : number
    personality: number
    moods      : number
  }
  figures : {
    task_id     : number
    thickness   : number
    boobs       : number
    bodies      : number
    butts       : number
    skin_details: string
  }
  uppers  : {
    task_id : number
    inverted: number
    puffy   : number
    areola  : number
    nipples : number
  }
  lowers  : {
    task_id        : number
    model          : number
    public         : number
    size           : number
    sheath         : number
    foreskin       : number
    genital_details: string
  }
  colors  : {
    task_id     : number
    theme       : number
    hair        : string
    eyes        : string
    outfits_main: string
    outfits_sub : string
    equips_main : string
    equips_sub  : string
    skin_main   : string
    skin_sub    : string
    nipples     : string
    genitals    : string
  }
}

const updateConfigsData:RequestConfigs = {
  weights: {
    model:      [0,1,2,3],
    theme:      [0,1,2,3],
    weathers:   [0,1,2,3],
    periods:    [0,1,2,3],
    angles:     [0,1,2,3],
    directions: [0,1,2,3],
    focuses:    [0,1,2,3]
  },
  phrases: {
    header:        "header__________TEST123",
    footer:        "footer__________TEST123",
    negative:      "negative________TEST123",
    request_order: "request_order___TEST123",
    playing_order: "playing_order___TEST123",
    posting_desc:  "posting_desc____TEST123",
    content_desc:  "content_desc____TEST123"
  }
}

const postConstantsData:RequestConstants = {
  create: [
    { category: "TTTTTT", is_lewd: false, name: "TEST_TTTTTT_NAME", value: "TEST_TTTTTT_VALUE" },
    { category: "EEEEEE", is_lewd: false, name: "TEST_EEEEEE_NAME", value: "TEST_EEEEEE_VALUE" },
    { category: "SSSSSS", is_lewd: false, name: "TEST_SSSSSS_NAME", value: "TEST_SSSSSS_VALUE" },
    { category: "TTTTTT", is_lewd: false, name: "TEST_TTTTTT_NAME", value: "TEST_TTTTTT_VALUE" }
  ],
  update: [],
  delete: []
}
const altrConstantsData:RequestConstants = {
  create: [
    { category: "AAAAAA", is_lewd: false, name: "TEST_AAAAAA_NAME", value: "TEST_AAAAAA_VALUE" },
    { category: "LLLLLL", is_lewd: false, name: "TEST_LLLLLL_NAME", value: "TEST_LLLLLL_VALUE" },
    { category: "TTTTTT", is_lewd: false, name: "TEST_TTTTTT_NAME", value: "TEST_TTTTTT_VALUE" },
  ],
  update: [
    { id:1, category: "ALTERED", is_lewd: true, name: "_NAMETTTTTTTEST_", value: "_VALUETTTTTTTEST_" },
    { id:3, category: "ALTERED", is_lewd: true, name: "_NAMEEEEEEETEST_", value: "_VALUEEEEEEETEST_" },
  ],
  delete: [
    { id:2, category: "SSSSSS", is_lewd: false, name: "TEST_SSSSSS_NAME", value: "TEST_SSSSSS_VALUE" },
    { id:4, category: "TTTTTT", is_lewd: false, name: "TEST_TTTTTT_NAME", value: "TEST_TTTTTT_VALUE" }
  ]
}

const postGroupData: RequestGroup = {
  name: "AAAAAA"
}
const patchGroupData: RequestGroup = {
  name: "BBBBBB"
}

const postPostData:RequestPosts = {
  task_id:        1,
  story:          "story___________Test",
  title_JP:       "title_JP________Test",
  title_EN:       "title_EN________Test",
  title_symbol:   "title_symbol____Test",
  picture_count:  "picture_count___Test",
  wallpaper_count:"wallpaper_count_Test",
  picture_URL:    "picture_URL_____Test",
  wallpaper_URL:  "wallpaper_URL___Test",
  notes: [
    "notes_notes_notes_notes_notes_🌞",
    "notes_notes_notes_notes_notes_🌞",
    "notes_notes_notes_notes_notes_🌞",
    "notes_notes_notes_notes_notes_🌞",
    "notes_notes_notes_notes_notes_🌞"
  ]
}
const patchPostData:RequestPosts = {
  task_id:        1,
  story:          "Test___________story",
  title_JP:       "Test________title_JP",
  title_EN:       "Test________title_EN",
  title_symbol:   "Test____title_symbol",
  picture_count:  "Test___picture_count",
  wallpaper_count:"Test_wallpaper_count",
  picture_URL:    "Test_____picture_URL",
  wallpaper_URL:  "Test___wallpaper_URL",
  notes: [
    "test_test_test_test_test_test_test_🌞",
    "test_test_test_test_test_test_test_🌞",
    "test_test_test_test_test_test_test_🌞",
    "test_test_test_test_test_test_test_🌞",
    "test_test_test_test_test_test_test_🌞"
  ]
}

const patchPrmptData:RequestPrompts = {
  task_id:    1,
  HEADER:     "HEADER_____Test",
  basis:      "basis______Test",
  faces:      "faces______Test",
  hairs:      "hairs______Test",
  figures:    "figures____Test",
  location:   "location___Test",
  outfits:    "outfits____Test",
  equips:     "equips_____Test",
  emotes:     "emotes_____Test",
  fluids:     "fluids_____Test",
  upper:      "upper______Test",
  lower:      "lower______Test",
  actions:    "actions____Test",
  posing:     "posing_____Test",
  additional: "additional_Test",
  FOOTER:     "FOOTER_____Test"
}
const postPrmptData:RequestPrompts = {
  task_id   : 1,
  HEADER    : "Test______HEADER",
  basis     : "Test_______basis",
  faces     : "Test_______faces",
  hairs     : "Test_______hairs",
  figures   : "Test_____figures",
  location  : "Test____location",
  outfits   : "Test_____outfits",
  equips    : "Test______equips",
  emotes    : "Test______emotes",
  fluids    : "Test______fluids",
  upper     : "Test_______upper",
  lower     : "Test_______lower",
  actions   : "Test_____actions",
  posing    : "Test______posing",
  additional: "Test__additional",
  FOOTER    : "Test______FOOTER"
}

const patchReqData:RequestRequests = {
  basis: {
    task_id:        1,
    model:          0,
    thickness:      0,
    theme:          0,
    species:        "Test_________species",
    species_details:"Test_species_details",
    traits:         "Test__________traits",
    traits_details: "Test__traits_details"
  },
  location: {
    task_id          : 1,
    weathers         : 0,
    periods          : 0,
    times            : 0,
    locations_details: "Test_locations_details"
  },
  outfits: {
    task_id        : 1,
    jobs           : "Test____________jobs",
    jobs_details   : "Test____jobs_details",
    outfits_details: "Test_outfits_details",
    equips_details : "Test__equips_details"
  },
  hairs: {
    task_id    : 1,
    size       : 0,
    hair_style : "Test__hair_style",
    bangs_style: "Test_bangs_style"
  },
  faces: {
    task_id    : 1,
    looks      : 0,
    eyes       : 0,
    personality: 0,
    moods      : 0
  },
  figures: {
    task_id     : 1,
    thickness   : 0,
    boobs       : 0,
    bodies      : 0,
    butts       : 0,
    skin_details: "Test_skin_details"
  },
  uppers: {
    task_id : 1,
    inverted: 0,
    puffy   : 0,
    areola  : 0,
    nipples : 0
  },
  lowers: {
    model          : 1,
    task_id        : 0,
    public         : 0,
    size           : 0,
    sheath         : 0,
    foreskin       : 0,
    genital_details: "Test_genital_details"
  },
  colors: {
    task_id     : 1,
    theme       : 0,
    hair        : "Test_________hair",
    eyes        : "Test_________eyes",
    outfits_main: "Test_outfits_main",
    outfits_sub : "Test__outfits_sub",
    equips_main : "Test__equips_main",
    equips_sub  : "Test___equips_sub",
    skin_main   : "Test____skin_main",
    skin_sub    : "Test_____skin_sub",
    nipples     : "Test______nipples",
    genitals    : "Test_____genitals"
  }
}
const postReqData:RequestRequests = {
  basis: {
    task_id:        1,
    model:          1,
    thickness:      2,
    theme:          3,
    species:        "species_________Test",
    species_details:"species_details_Test",
    traits:         "traits__________Test",
    traits_details: "traits_details__Test"
  },
  location: {
    task_id          : 1,
    weathers         : 1,
    periods          : 2,
    times            : 3,
    locations_details: "locations_details_Test"
  },
  outfits: {
    task_id        : 1,
    jobs           : "jobs____________Test",
    jobs_details   : "jobs_details____Test",
    outfits_details: "outfits_details_Test",
    equips_details : "equips_details__Test"
  },
  hairs: {
    task_id    : 1,
    size       : 1,
    hair_style : "hair_style__Test",
    bangs_style: "bangs_style_Test"
  },
  faces: {
    task_id    : 1,
    looks      : 1,
    eyes       : 2,
    personality: 3,
    moods      : 4
  },
  figures: {
    task_id     : 1,
    thickness   : 1,
    boobs       : 2,
    bodies      : 3,
    butts       : 4,
    skin_details: "skin_details_Test"
  },
  uppers: {
    task_id : 1,
    inverted: 1,
    puffy   : 2,
    areola  : 3,
    nipples : 4
  },
  lowers: {
    model          : 1,
    task_id        : 1,
    public         : 2,
    size           : 3,
    sheath         : 4,
    foreskin       : 5,
    genital_details: "genital_details_Test"
  },
  colors: {
    task_id     : 1,
    theme       : 0,
    hair        : "hair_________Test",
    eyes        : "eyes_________Test",
    outfits_main: "outfits_main_Test",
    outfits_sub : "outfits_sub__Test",
    equips_main : "equips_main__Test",
    equips_sub  : "equips_sub___Test",
    skin_main   : "skin_main____Test",
    skin_sub    : "skin_sub_____Test",
    nipples     : "nipples______Test",
    genitals    : "genitals_____Test"
  }
}