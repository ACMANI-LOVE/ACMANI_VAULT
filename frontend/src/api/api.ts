interface APIRequest {
  prmText?: string
  request?: object
}

// "configs": `http://localhost:8000/configs/`,
export const getConfigsAPI    = () => { fetcher("GET", `http://localhost:8000/configs/`)}
export const postConfigsAPI   = ({request}:APIRequest) => { fetcher("POST", `http://localhost:8000/configs/`, request)}
export const putConfigsAPI    = ({prmText,request}:APIRequest) => { fetcher("PUT" , `http://localhost:8000/configs/${prmText}/`, request)}

// "groups": `http://localhost:8000/groups/`,
export const getGroupsAPI    = () => { fetcher("GET" , `http://localhost:8000/groups/`)}
export const postGroupsAPI   = ({request}:APIRequest) => { fetcher("POST", `http://localhost:8000/groups/`, request)}
export const patchGroupsAPI  = ({prmText,request}:APIRequest) => { fetcher("PATCH" , `http://localhost:8000/groups/${prmText}/`, request)}
export const deleteGroupsAPI = ({prmText,request}:APIRequest) => { fetcher("DELETE", `http://localhost:8000/groups/${prmText}/`)}

// "tasks": `http://localhost:8000/tasks/`,
export const getTasksAPI    = ({prmText}:APIRequest) => { fetcher("GET", `http://localhost:8000/tasks/${prmText}/`)}

// "posts": `http://localhost:8000/posts/`,
export const postPostsAPI   = ({request}:APIRequest) => { fetcher("POST" , `http://localhost:8000/posts/`     , request)}
export const patchPostsAPI  = ({prmText,request}:APIRequest) => { fetcher("PATCH", `http://localhost:8000/posts/${prmText}/`, request)}

// "prompts": `http://localhost:8000/prompts/`,
export const postPromptsAPI   = ({request}:APIRequest) => { fetcher("POST" , `http://localhost:8000/prompts/`     , request)}
export const patchPromptsAPI  = ({prmText,request}:APIRequest) => { fetcher("PATCH", `http://localhost:8000/prompts/${prmText}/`, request)}

// "requests": `http://localhost:8000/requests/`,
export const postRequestsAPI   = ({request}:APIRequest) => { fetcher("POST" , `http://localhost:8000/requests/`     , request)}
export const patchRequestsAPI  = ({prmText,request}:APIRequest) => { fetcher("PATCH", `http://localhost:8000/requests/${prmText}/`, request)}


const fetcher = async (method:string, url:string, request?:object) => {
  console.log(JSON.stringify(request))
  try {
    const response = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request)
    });
    const responseData = await response.json();
    return responseData
  } catch (err) {
    alert(err)
  }
}