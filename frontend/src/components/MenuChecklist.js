import React, { useEffect, useState } from "react"

export const MenuChecklist = (props) => {
    const [fooditems, setFoodItems] = useState([]);
    const [masterChecked, setMasterChecked] = useState(false);
    const [checkedList, setCheckedList] = useState([]);

    useEffect(() => {
        setFoodItems(props.menu);
        console.log(props.menu)
    }, [props]);

    function onMasterCheck(e) {
        let tempList = fooditems;
        tempList.map((item) => (item.selected = e.target.checked));

        setMasterChecked(e.target.checked);
        setFoodItems(tempList);
        setCheckedList(tempList.filter((e) => e.selected));
    }

    function onItemCheck(e, fooditem) {
        let tempList = fooditems;
        tempList.map((item) => {
            if (item.name === fooditem.name) {
                item.selected = e.target.checked;
            }
            return item;
        });

        const totalItems = fooditems.length;
        const totalCheckedItems = tempList.filter((e) => e.selected).length;

        setMasterChecked(totalCheckedItems === totalItems);
        setFoodItems(tempList);
        setCheckedList(tempList.filter((e) => e.selected))
    }

    function showNutritionForChecked() {
        let tempList = checkedList;
        let caloriesTotal = 0.0;
        let fatTotal = 0.0;
        let carbsTotal = 0.0;
        let proteinTotal = 0.0;
        for (let i = 0; i < tempList.length; i++) {
            caloriesTotal += Number(tempList[i].calories);
            fatTotal += Number(tempList[i].fat);
            carbsTotal += Number(tempList[i].carbohydrates);
            proteinTotal += Number(tempList[i].protein);
        }

        let str = `Your meal consists of ${caloriesTotal}g of calories, ${fatTotal}g of fat, ${carbsTotal}g of carbohydrates, and ${proteinTotal}g of protein.`;
        return (str);
    }

    return (
        <div className="container">
          <div className="row">
            <div className="col-md-12">
                <table className="table">
                    <thead>
                    <tr>
                        <th scope="col">
                        <input
                            type="checkbox"
                            className="form-check-input"
                            checked={masterChecked}
                            id="mastercheck"
                            onChange={(e) => onMasterCheck(e)}
                        />
                        </th>
                        <th scope="col">Item name</th>
                        <th scope="col">Calories</th>
                        <th scope="col">Fat</th>
                        <th scope="col">Carbohydrates</th>
                        <th scope="col">Protein</th>
                    </tr>
                    </thead>
                    <tbody>
                    {fooditems.map((item) => (
                        <tr key={item.name} className={item.selected ? "selected" : ""}>
                        <th scope="row">
                            <input
                            type="checkbox"
                            checked={item.selected}
                            className="form-check-input"
                            id="rowcheck{item.name}"
                            onChange={(e) => onItemCheck(e, item)}
                            />
                        </th>
                        <td>{item.name}</td>
                        <td>{item.calories}</td>
                        <td>{item.fat}</td>
                        <td>{item.carbohydrates}</td>
                        <td>{item.protein}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
                <div className="row">
                    <code>{showNutritionForChecked()}</code>
                </div>
            </div>
          </div>
        </div>
      );
}
