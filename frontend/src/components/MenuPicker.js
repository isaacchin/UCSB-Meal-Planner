import axios from "axios";
import React, { useEffect, useState } from "react"

export const MealPicker = (props) => {
    const [selectedCommons, setDiningCommons] = useState()
    function changeDiningCommons(e) {
        setDiningCommons(e.target.value);
    }

    const [mealsList, setMealsList] = useState([]);
    const [selectedMeal, setMeal] = useState([]);
    const [readyToRenderTable, setTableStatus] = useState(false);

    function changeMeal(e) {
        const selectedIndex = e.target.options.selectedIndex;
        if (selectedIndex !== 0) {
            const meal = mealsList[e.target.options[selectedIndex].getAttribute('data_key')].food_items;
            setMeal(meal);
            setTableStatus(true);
            props.parentMenuCallback(meal);
            props.parentRenderCallback(true);
        }
        else {
            setMeal([]);
            setTableStatus(false);
            props.parentMenuCallback([]);
            props.parentRenderCallback(false);
        }
        
        
    }

    useEffect(() => {
        const fetchMeals = async () => {
            const APIString = 'http://localhost:8000/api/diningmenu/commons/';
            const CommonsName = selectedCommons;
            const QueryString = `${APIString}${CommonsName}`;
            const result = await axios(QueryString);
            setMealsList(result.data)
        }

        fetchMeals();
    }, [selectedCommons]);

    return (
        <div>
            <div>
                <div>
                    Choose the dining commons:
                </div>
                <select onChange={changeDiningCommons} name="commons" id="commons-select">
                    <option value="dummy">Select a dining commons</option>
                    <option value="De La Guerra">De La Guerra</option>
                    <option value="Ortega">Ortega</option>
                </select>
            </div>
            <div>
                <div>
                    Choose the menu to build your meal from:
                </div>
                <select onChange={changeMeal} name="meals" id="meals-select">
                    <option value={[{"name": "dummy"}]}>Select a menu</option>
                    {mealsList.map((option, index) => (
                        <option key={index} data_key={index} value={option.name}>
                            {option.name}
                        </option>
                    ))}
                </select>
            </div>
        </div>
        
    );
}