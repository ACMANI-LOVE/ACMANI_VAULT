import { useContext, useState, useEffect, useCallback, ReactNode } from "react"
import { FrameBox, FlexBox, LargeLabel, ButtonComponent, SmallLabel, MediumLabel } from "../atoms/atoms"
import useListPicker from "../hooks/useListPicker"
import { StateContext, DataContext } from "../hooks/useProviders"
import useCounterField from "../hooks/useCounterField"

const GroupSelector = () => {
  const { groupState } = useContext(StateContext)
  const { group } = useContext(DataContext)

  const [taskSelect, setTaskSelect] = useState(0)
  const [ListPiker, selectIdx] = useListPicker({selectList:group.state, initialIndex:taskSelect})
  useEffect(()=>setTaskSelect(selectIdx),[selectIdx])

  const handleClickLoad   = () => {groupState.setState("CONFIRM")}
  const handleClickCreate = () => {groupState.setState("EDIT")}

  return (<FrameBox direction={"row"} padding={"0.25em"} width={"100%"} align={"center"} justify={"center"}>
    <FlexBox fx={8}>
      <LargeLabel text={"Period:"}/>
      <FrameBox direction={"row"} padding={"0.25em"} width={"100%"} align={"center"} justify={"space-around"}>
        <ListPiker/>
      </FrameBox>
    </FlexBox>
    <FlexBox fx={2}>
      <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-around"}>
        <ButtonComponent label={"Load"} textSize={"caption"} btnType={"contained"} onClick={handleClickLoad  }/>
        <ButtonComponent label={"New"}  textSize={"caption"} btnType={"contained"} onClick={handleClickCreate}/>
      </FrameBox>
    </FlexBox>
  </FrameBox>)
}

export default GroupSelector

export const GroupEditor = () => {
  const { groupState } = useContext(StateContext)
  const { group } = useContext(DataContext)

  const now = new Date().toLocaleDateString()
  const [DatePicker, dateString] = useDatePicker({initialDateStr:now})

  const handleClickAdd  = () => {groupState.setState("CONFIRM")}
  const handleClickBack = () => {groupState.setState("SELECT")}

  return (<FrameBox direction={"row"} padding={"0.25em"} width={"100%"} align={"center"} justify={"center"}>
    <LargeLabel text={"Period:"}/>
    <FlexBox fx={8}>
      <FlexBox fx={3}>
        <DatePicker/>
      </FlexBox>
      <FlexBox fx={1}>
        <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-around"}>
          <MediumLabel text={`-to: ${dateString}`}/>
        </FrameBox>
      </FlexBox>
    </FlexBox>
    <FlexBox fx={2}>
      <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-around"}>
        <ButtonComponent label={"Add"}  textSize={"caption"} btnType={"contained"} onClick={handleClickAdd }/>
        <ButtonComponent label={"Back"} textSize={"caption"} btnType={"contained"} onClick={handleClickBack}/>
      </FrameBox>
    </FlexBox>
  </FrameBox>)
}

interface DateTimePickerProps {
  initialDateStr:string
}
type DateTimePickerReturns = [
  DateTimePicker: ()=>ReactNode,
  dateString: string
]
const useDatePicker = ({initialDateStr}:DateTimePickerProps) => {
  const [dateString, setDateString] = useState(initialDateStr)
  const current = new Date(dateString)
  const currentDay = new Date(current.getFullYear(),current.getMonth()+1,0).getDate()

  const [year    , setYear    ] = useState(current.getFullYear())
  const [monthIdx, setMonthIdx] = useState(current.getMonth())
  const [dateIdx , setDateIdx ] = useState(current.getDate()-1)
  const [maxDays , setMaxDays ] = useState(currentDay)

  useEffect(()=>{
    const days = new Date(year,monthIdx+1,0).getDate()
    // console.log(`${dateIdx+1} < ${days} = ${(dateIdx+1 < days)}`)
    // const upd = (dateIdx+1 < days)
    // ? new Date(year,monthIdx,dateIdx+1)
    // : new Date(year,monthIdx+1,0)
    // console.log(upd.toLocaleDateString())
    setMaxDays(days)
    // setDateString(upd.toLocaleDateString())
  // },[year,monthIdx,dateIdx])
  },[year,monthIdx])

  useEffect(()=>{

  },[dateIdx])

  const YearSelector = useCallback(() => {
      const [YearCounter, yearValue   ] = useCounterField({initialValue: year})
      useEffect(()=>setYear(yearValue),[yearValue])
      return (<FrameBox align={"center"} justify={"center"}>
      <SmallLabel text={"year:" }/>
      <YearCounter/>
    </FrameBox>)
  },[current])

  const MonthSelector = useCallback(() => {
    const [MonthPicker, monthUpdIdx ] = useListPicker  ({
      selectList:Array.from({length: 12},(_, idx)=>`${idx+1}`),
      initialIndex:monthIdx,
      noHyphen:true
    })
    useEffect(()=>setMonthIdx(monthUpdIdx),[monthUpdIdx])
    return (<FrameBox align={"center"} justify={"center"}>
      <SmallLabel text={"month:"}/>
      <MonthPicker/>
    </FrameBox>)
  },[current])

  const DateSelector = useCallback(() => {
    const [DatePicker,  dateUpdIdx  ] = useListPicker  ({
      selectList:Array.from({length: maxDays},(_, idx)=>`${idx+1}`),
      initialIndex:dateIdx,
      noHyphen:true
    })
    useEffect(()=>{
      const updDate = (dateUpdIdx+1 < maxDays) ? dateUpdIdx : maxDays -1
      setDateIdx(updDate)
    },[dateUpdIdx,maxDays])
    return (<FrameBox align={"center"} justify={"center"}>
      <SmallLabel text={"day:"  }/>
      <DatePicker/>
    </FrameBox>)
  },[current,maxDays])

  const DateTimePicker = useCallback(()=>{
    return (<FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-evenly"}>
      <FlexBox fx={3}>
        <YearSelector/>
      </FlexBox>
      <FlexBox fx={2}>
        <MonthSelector/>
      </FlexBox>
      <FlexBox fx={2}>
        <DateSelector/>
      </FlexBox>
    </FrameBox>)
  },[current,maxDays])
  return [DateTimePicker, dateString] as DateTimePickerReturns
}

interface MaxDaysProps {
  year:number
  monthIdx:number
}
type MaxDaysReturns = [
  maxDays:number
]
const useMaxDays = ({year,monthIdx}:MaxDaysProps) => {
  return [new Date(year,monthIdx,0).getDate()] as MaxDaysReturns
}