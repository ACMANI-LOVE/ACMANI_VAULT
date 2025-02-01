import { useContext, useEffect, ReactNode, useState } from "react"
import { FrameBox, ButtonComponent, LargeLabel, FlexBox } from "../atoms/atoms"
import useListPicker from "../hooks/useListPicker"
import { GroupState, StateContext } from "../hooks/useProviders"
import useCounterField from "../hooks/useCounterField"
import GroupSelector, { GroupEditor } from "./groupSelector"

const GroupManager = () => {
  const { groupState } = useContext(StateContext)

  const [date, setDate] = useState(new Date())

  const handleClickChange = () => {groupState.setState("SELECT")}
  const handleClickDelete = () => {groupState.setState("SELECT")}

  // const GroupEditor = () => {
  //   const now = new Date()
  //   const [current, setCurrent] = useState(now)
  //   const [month, setMonth] = useState(now.getMonth()+1)
  //   const [date , setDate ] = useState(now.getDate()   )

  //   // const [monthList, dateList] = useYMDList({year:current.getFullYear(), month:current.getMonth()-1})
  //   const monthList = Array.from({length:12               },(_,idx)=>`${idx+1}`)
  //   const dateList  = Array.from({length:current.getDate()},(_,idx)=>`${idx+1}`)

  //   const [MonthPiker,  monthIdx ] = useListPicker({selectList:monthList, initialIndex:month, noHyphen:true })
  //   const [DatePiker,   dateIdx  ] = useListPicker({selectList:dateList,  initialIndex:date-1 , noHyphen:true })
  //   useEffect(()=>{
  //     // const newMonth = Number(monthList[0])
  //     console.log("newMonth:"+(monthIdx+1))
  //     const maxDays = new Date(yearValue,monthIdx,0).getDate()
  //     console.log("maxDays:"+maxDays)
  //     const newDate  = (maxDays>=Number(dateList[dateIdx])) ? Number(dateList[dateIdx]) : maxDays
  //     console.log("newDate:"+newDate)

  //     const updateDate = new Date(yearValue,monthIdx,newDate)
  //     console.log("current:"+current.toLocaleDateString())
  //     console.log("updateDate:"+updateDate.toLocaleDateString())
  //     setCurrent(updateDate)
  //   },[yearValue,monthIdx,dateIdx])
  //   useEffect(()=>{
  //     setMonth(current.getMonth())
  //     setDate (current.getDate()   )
  //   },[current])

  //   return (
  //   <FrameBox padding={"0.25em"} gap={"0.5em"} direction={"row"} width="100%">
  //     <FlexBox fx={2}>
  //       <YearCounter/>
  //     </FlexBox>
  //     <FlexBox fx={1}>
  //       <MonthPiker/>
  //     </FlexBox>
  //     <FlexBox fx={1}>
  //       <DatePiker/>
  //     </FlexBox>
  //     {current.toLocaleDateString()}
  //   </FrameBox>
  //   )
  // }
  const GroupLabel  = () => {
    return (
    <FrameBox padding={"0.25em"} gap={"0.5em"} direction={"row"} width="100%">
      <ButtonComponent label={"Change"} textSize={"caption"} btnType={"contained"} onClick={handleClickChange}/>
      <ButtonComponent label={"Delete"} textSize={"caption"} btnType={"contained"} onClick={handleClickDelete}/>
    </FrameBox>
    )
  }
  const PickerItem: Record<GroupState, ReactNode> = {
    "-1": <>No Items</>,
    "SELECT":  <GroupSelector/>,
    "EDIT":    <GroupEditor/>,
    "CONFIRM": <GroupLabel />
  }
  return (<FrameBox direction={"row"} width={"95%"} align={"center"} justify={"center"}>
    {PickerItem[groupState.state]}
  </FrameBox>
  )
}

export default GroupManager



interface YMDListProps {
  year:any
  month:any
}
type YMDListReturns = [
  monthList: string[],
  dateList:  string[],
]
const useYMDList = ({year,month}:YMDListProps) => {
  const daysInMonth = new Date(year,month,0).getDate()
  const monthList = ["1","2","3","4","5","6","7","8","9","10","11","12"]
  const dateList  = Array.from({length: daysInMonth }, (_, idx) => (idx + 1).toString())
  return [ monthList, dateList ] as YMDListReturns
}