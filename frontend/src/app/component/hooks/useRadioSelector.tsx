import { BaseSyntheticEvent, ReactNode, useCallback, useState } from "react"
import RadioList from "../molecules/radioGroup"

interface RadioSelectorProps {
  selectList: string[]
  initialIndex: number
}
type RadioSelectorReturns = [
  RadioSelector: ()=>ReactNode,
  selectIdx: number
]
const useRadioSelector = ({selectList, initialIndex}:RadioSelectorProps) => {
  const [selectIdx,setSelectIdx] = useState(initialIndex)
  const RadioSelector = useCallback(() => {
    const handleChangeSelect = (e:BaseSyntheticEvent) => setSelectIdx(e.target.value)
    return (<RadioList list={selectList} select={selectIdx} onChange={handleChangeSelect}/>)
  },[selectList])
  return [RadioSelector, selectIdx ] as RadioSelectorReturns
}

export default useRadioSelector