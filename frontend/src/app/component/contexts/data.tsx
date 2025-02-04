import { StateType } from "@/const/type"
import { createContext } from "react"

export type GroupListData = StateType<Group[]>
export type GroupData     = StateType<Group>
export type TaskListData = StateType<Task[]>
export type TaskData     = StateType<Task>

export type DataContextType = {
  groupList: GroupListData,
  group:     GroupData,
  taskList: TaskListData,
  task:     TaskData,
}

export const DataContext = createContext<DataContextType>({
  groupList: { state:[], setState:()=>{}},
  group:     { state:{
    id:   0,
    name: ""
  }, setState:()=>{}},
  task:     { state:{
    id:   0,
    index: 0,
    name: ""
  }, setState:()=>{}},
  taskList: { state:[], setState:()=>{}},
})

export default DataContext

interface Task {
  id:   number
  index:number
  name: string
}
interface Group {
  id:   number
  name: string
}