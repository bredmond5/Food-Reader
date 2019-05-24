//
//  SwiftChartsViewController.swift
//  C++
//
//  Created by Sai Kathika on 5/19/19.
//  Copyright © 2019 Sai Kathika. All rights reserved.
//

import UIKit
import SwiftCharts

class SwiftsChartsViewController: UIViewController{
    var chartView: BarsChart!

    override func viewDidLoad() {
        super.viewDidLoad()
//        add_products(Int8("Lays")!)
      //  add_products(UnsafeMutablePointer<Int8>?)
        add_products("Apple")
      //  add_products(UnsafeMutablePointer<Int8>?("pear")!)
        getData(30, 25, 38)
        func getPersonName() -> UnsafePointer<Int8>{
        let cstr = getPersonName()
            
            let name = String.fromCString(cstr)
        //free(UnsafeMutablePointer(cstr))
        
            print(name)}
        let average = (return_products_scanned()+return_products_searched()+return_products_added()/3)
        let chartConfig = BarsChartConfig(valsAxisConfig: ChartAxisConfig(from:0,to:average,by:5))

        let frame = CGRect(x: 5, y: 90, width: self.view.frame.width, height: 450)
       // getData(30, 25, 38)
        update_products_searched()
        update_products_scanned()
        update_products_added()
        let chart = BarsChart(frame: frame, chartConfig: chartConfig, xTitle: "Products", yTitle: "Number of Scans per Session", bars: [                                                                             ("Scanned",return_products_scanned()),("Searched",return_products_searched()),("Inputed",return_products_added()),],

        color: UIColor.red, barWidth: 60)
        self.view.addSubview(chart.view)
        self.chartView = chart
    }
    func storeData(){
        UserDefaults.standard.set(return_products_scanned(),forKey: "scanned")
        //defaults?.synchronize()
    }
    func getData1(){
        let data = UserDefaults.value(forKey: "scanned")
        var x = return_products_scanned()
        x = data as! Double
        set_scanned(x)
    }
}




    

