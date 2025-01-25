interface APIRequest {
  parameter?: string
  request?: object
}

// "configs": `http://localhost:8000/configs/`,
export const getConfigsAPI    = ()                     => fetcher("GET",  `http://localhost:8000/configs/information`)
export const postConfigsAPI   = ({request}:APIRequest) => fetcher("POST", `http://localhost:8000/configs/`, request)
export const putConfigsAPI    = ({request}:APIRequest) => fetcher("PUT",  `http://localhost:8000/configs/update/`, request)

// "groups": `http://localhost:8000/groups/`,
export const getGroupsAPI    = ()                               => fetcher("GET" ,   `http://localhost:8000/groups/`)
export const postGroupsAPI   = ({request}:APIRequest)           => fetcher("POST",   `http://localhost:8000/groups/`, request)
export const patchGroupsAPI  = ({parameter,request}:APIRequest) => fetcher("PATCH" , `http://localhost:8000/groups/${parameter}/`, request)
export const deleteGroupsAPI = ({parameter}:APIRequest)         => fetcher("DELETE", `http://localhost:8000/groups/${parameter}/`)

// "tasks": `http://localhost:8000/tasks/`,
export const getTasksAPI    = ({parameter}:APIRequest) => fetcher("GET", `http://localhost:8000/tasks/${parameter}/`)

// "posts": `http://localhost:8000/posts/`,
export const postPostsAPI   = ({request}:APIRequest)           => fetcher("POST",  `http://localhost:8000/posts/`     , request)
export const patchPostsAPI  = ({parameter,request}:APIRequest) => fetcher("PATCH", `http://localhost:8000/posts/${parameter}/`, request)

// "prompts": `http://localhost:8000/prompts/`,
export const postPromptsAPI   = ({request}:APIRequest)           => fetcher("POST",  `http://localhost:8000/prompts/`     , request)
export const patchPromptsAPI  = ({parameter,request}:APIRequest) => fetcher("PATCH", `http://localhost:8000/prompts/${parameter}/`, request)

// "requests": `http://localhost:8000/requests/`,
export const postRequestsAPI   = ({request}:APIRequest)           => fetcher("POST",  `http://localhost:8000/requests/`, request)
export const patchRequestsAPI  = ({parameter,request}:APIRequest) => fetcher("PATCH", `http://localhost:8000/requests/${parameter}/`, request)


const fetcher = async (method:string, url:string, request?:object) => {
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