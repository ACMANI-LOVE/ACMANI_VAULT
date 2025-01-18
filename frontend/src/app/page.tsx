'use client'
import { Box, Button, Container } from "@mui/material";
import { deleteGroupsAPI, getConfigsAPI, getGroupsAPI, getTasksAPI, patchGroupsAPI, patchPostsAPI, patchPromptsAPI, patchRequestsAPI, postConfigsAPI, postGroupsAPI, postPostsAPI, postPromptsAPI, postRequestsAPI, putConfigsAPI } from "@/api/api"

const Home = () => {
  const getConfigs    = () => getConfigsAPI   ()
  const putConfigs    = () => putConfigsAPI   ({prmText:"1", request:{test:0}})
  const postConfigs   = () => postConfigsAPI  ({request:{isLewd:true}})
  const getGroups     = () => getGroupsAPI    ()
  const postGroups    = () => postGroupsAPI   ({request:{test:0}})
  const patchGroups   = () => patchGroupsAPI  ({prmText:"1", request:{test:0}})
  const deleteGroups  = () => deleteGroupsAPI ({prmText:"1"})
  const getTasks      = () => getTasksAPI     ({prmText:"1"})
  const postPosts     = () => postPostsAPI    ({request:{}})
  const patchPosts    = () => patchPostsAPI   ({prmText:"1", request:{test:0}})
  const postPrompts   = () => postPromptsAPI  ({request:{}})
  const patchPrompts  = () => patchPromptsAPI ({prmText:"1", request:{test:0}})
  const postRequests  = () => postRequestsAPI ({request:{}})
  const patchRequests = () => patchRequestsAPI({prmText:"1", request:{test:0}})
  return (<Box display={"flex"} flexDirection={"column"}>
    Config
    <Button variant="contained" onClick={getConfigs    }>getConfigsAPI   </Button>
    <Button variant="contained" onClick={putConfigs    }>putConfigsAPI   </Button>
    <Button variant="contained" onClick={postConfigs   }>postConfigsAPI  </Button>
    Groups
    <Button variant="contained" onClick={getGroups     }>getGroupAPI     </Button>
    <Button variant="contained" onClick={postGroups    }>postGroupAPI    </Button>
    <Button variant="contained" onClick={patchGroups   }>patchGroupAPI   </Button>
    <Button variant="contained" onClick={deleteGroups  }>deleteGroupAPI  </Button>
    Tasks
    <Button variant="contained" onClick={getTasks      }>getTaskAPI      </Button>
    Posts
    <Button variant="contained" onClick={postPosts     }>postPostsAPI    </Button>
    <Button variant="contained" onClick={patchPosts    }>patchPostsAPI   </Button>
    Prompts
    <Button variant="contained" onClick={postPrompts   }>postPromptsAPI  </Button>
    <Button variant="contained" onClick={patchPrompts  }>patchPromptsAPI </Button>
    Requests
    <Button variant="contained" onClick={postRequests  }>postRequestsAPI </Button>
    <Button variant="contained" onClick={patchRequests }>patchRequestsAPI</Button>
  </Box>);
}
export default Home