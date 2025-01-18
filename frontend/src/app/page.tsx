'use client'
import { Button } from "@mui/material";
import { deleteGroupsAPI, getConfigsAPI, getGroupsAPI, getTasksAPI, patchGroupsAPI, patchPostsAPI, patchPromptsAPI, patchRequestsAPI, postConfigsAPI, postGroupsAPI, postPostsAPI, postPromptsAPI, postRequestsAPI, putConfigsAPI } from "@/api/api"

const Home = () => {
  const getConfigs    = () => getConfigsAPI   ()
  const putConfigs    = () => putConfigsAPI   ({request:{}})
  const postConfigs   = () => postConfigsAPI  ({request:{}})
  const getGroups     = () => getGroupsAPI    ()
  const postGroups    = () => postGroupsAPI   ({request:{}})
  const patchGroups   = () => patchGroupsAPI  ({prmText:"", request:{}})
  const deleteGroups  = () => deleteGroupsAPI ({prmText:"", request:{}})
  const getTasks      = () => getTasksAPI     ({prmText:""})
  const postPosts     = () => postPostsAPI    ({request:{}})
  const patchPosts    = () => patchPostsAPI   ({prmText:"", request:{}})
  const postPrompts   = () => postPromptsAPI  ({request:{}})
  const patchPrompts  = () => patchPromptsAPI ({prmText:"", request:{}})
  const postRequests  = () => postRequestsAPI ({request:{}})
  const patchRequests = () => patchRequestsAPI({prmText:"", request:{}})
  return (<div>
    <Button variant="contained" onClick={getConfigs    }>getConfigsAPI   </Button>
    <Button variant="contained" onClick={putConfigs    }>putConfigsAPI   </Button>
    <Button variant="contained" onClick={postConfigs   }>postConfigsAPI  </Button>
    <Button variant="contained" onClick={getGroups     }>getGroupAPI     </Button>
    <Button variant="contained" onClick={postGroups    }>postGroupAPI    </Button>
    <Button variant="contained" onClick={patchGroups   }>patchGroupAPI   </Button>
    <Button variant="contained" onClick={deleteGroups  }>deleteGroupAPI  </Button>
    <Button variant="contained" onClick={getTasks      }>getTaskAPI      </Button>
    <Button variant="contained" onClick={postPosts     }>postPostsAPI    </Button>
    <Button variant="contained" onClick={patchPosts    }>patchPostsAPI   </Button>
    <Button variant="contained" onClick={postPrompts   }>postPromptsAPI  </Button>
    <Button variant="contained" onClick={patchPrompts  }>patchPromptsAPI </Button>
    <Button variant="contained" onClick={postRequests  }>postRequestsAPI </Button>
    <Button variant="contained" onClick={patchRequests }>patchRequestsAPI</Button>
  </div>);
}
export default Home