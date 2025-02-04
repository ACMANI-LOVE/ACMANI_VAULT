import { useContext, useEffect, useState } from "react"
import { DividerLine, FrameBox, LargeLabel, MediumLabel, SmallLabel } from "../../atoms/atoms"
import DataContext from "../../contexts/data"
import useRadioSelector from "../../hooks/useRadioSelector"

  const TaskSelector = () => {
    const { group, taskList, task } = useContext(DataContext)
    const selectList = taskList.state.map((item)=>item.name)

  const [taskSelect, setTaskSelect] = useState(0)
    const [RadioSelector, selectIdx] = useRadioSelector({selectList, initialIndex:taskSelect})
    useEffect(()=>{
      task.setState(taskList.state[selectIdx])
      setTaskSelect(selectIdx)
    },[selectIdx])

    const SelectField = () => (selectList)
      ? <RadioSelector/>
      : <FrameBox padding={"0.5em"} justify="center" align="center">
        <MediumLabel text={" - No Items. - "}/>
      </FrameBox>
    return (<FrameBox padding={"0.5em"} direction={"column"} width={"100%"}>
      <LargeLabel text={"Task List"}/>
      <FrameBox direction={"column"}>
        <SmallLabel text={`Now Select${0}`}/>
        <SmallLabel text={`Now Select${0}`}/>
      </FrameBox>
      <DividerLine/>
      <SelectField/>
    </FrameBox>)
  }

  export default TaskSelector