import { StateType } from "@/const/type"
import { createContext, ReactNode, useCallback, useContext, useEffect, useState } from "react"
import { FlexBox, FrameBox, SmallLabel } from "../atoms/atoms"
import useCounterField from "./useCounterField"
import useListPicker from "./useListPicker"

interface DatePickerFieldProps {
  initialDate:string
}
type DatePickerFieldReturns = [
  DatePickerField: ()=>ReactNode,
  dateString: string,
]

const useDatePickerField = ({initialDate}:DatePickerFieldProps) => {
  const [dateString, setDateString] = useState(initialDate)

  const DateContext = createContext<StateType<string>>({
    state: dateString,
    setState: setDateString
  })

  const YearField = useCallback(() => {
    const { state, setState } = useContext(DateContext)
    const date = new Date(state)
    const [YearCounter, yearValue   ] = useCounterField({initialValue: date.getFullYear()})

    useEffect(()=>{
      const update = new Date(date)
      update.setFullYear(yearValue)
      setState(update.toLocaleDateString())
    },[yearValue])

    return (<FrameBox width={"100%"} align={"baseline"} justify={"center"}>
      <SmallLabel text={"year:" }/>
      <YearCounter/>
    </FrameBox>)
  },[DateContext])

  const MonthField = useCallback(() => {
    const { state, setState } = useContext(DateContext)
    const date = new Date(state)
    const monthList = Array.from({length:12},(_,idx)=>(idx+1).toString())
    const [MonthPicker, monthIdx   ] = useListPicker({
      selectList:monthList,
      initialIndex:date.getMonth(),
      noHyphen:true
    })

    useEffect(()=>{
      const update = new Date(date)
      update.setMonth(monthIdx)
      setState(update.toLocaleDateString())
    },[monthIdx])

    return (<FrameBox width={"100%"} align={"baseline"} justify={"center"}>
      <SmallLabel text={"month:" }/>
      <MonthPicker/>
    </FrameBox>)
  },[DateContext])

  const DateField = useCallback(() => {
    const { state, setState } = useContext(DateContext)
    const date = new Date(state)
    const days = new Date(date.getFullYear(),date.getMonth()+1,0).getDate()
    const dateList = Array.from({length:days},(_,idx)=>(idx+1).toString())
    const [DatePicker, dateIdx   ] = useListPicker({
      selectList:dateList,
      initialIndex:date.getDate()-1,
      noHyphen:true
    })

    useEffect(()=>{
      const update = new Date(date)
      update.setDate(dateIdx+1)
      setState(update.toLocaleDateString())
    },[dateIdx])

    return (<FrameBox width={"100%"} align={"baseline"} justify={"center"}>
      <SmallLabel text={"date:" }/>
      <DatePicker/>
    </FrameBox>)
  },[DateContext])

  const DatePickerField = useCallback(() => {
    return (<FrameBox direction={"row"} padding={"0.25em"} width={"100%"} align={"center"} justify={"space-between"}>
      <DateContext.Provider value={{state:dateString, setState:setDateString}}>
        <FlexBox fx={2}>
          <YearField/>
        </FlexBox>
        <FlexBox fx={1}>
        <MonthField/>
          </FlexBox>
        <FlexBox fx={1}>
          <DateField/>
        </FlexBox>
      </DateContext.Provider>
    </FrameBox>)
  },[DateContext, dateString])

  return [ DatePickerField, dateString, ] as DatePickerFieldReturns
}


export default useDatePickerField