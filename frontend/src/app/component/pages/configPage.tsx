import { FrameBox, LargeLabel } from "../atoms/atoms"
import MapperListComponents from "../template/mapperLists"
import ParametersComponents from "../template/parameters"

  const ConfigPage = () => {
    const ConfigItems = {
      "-1": <>No Items</>,
      "Parameters": <ParametersComponents/>,
      "MapperList": <MapperListComponents/>,
    }
    return (<FrameBox width="100%" align="center" justify="center" bgColor="#00F5">
      {ConfigItems["-1"]}
    </FrameBox>)
  }
  export default ConfigPage