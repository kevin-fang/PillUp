//
//  ViewController.swift
//  PillUp
//
//  Created by Shayan on 9/16/18.
//  Copyright © 2018 Shayan. All rights reserved.
//

import UIKit
import SnapKit
import Alamofire
//import Charts

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    var tableView : UITableView!
    var profileImageView : UIImageView!
    var userNameLabel : UILabel!
    var todayLabel : UILabel!
    var myPillsLabel : UILabel!
    var addButton : UIButton!
    var myPillsLine : UIView!
    var data = [CTableViewCell]()
//    var chartView : BarChartView!
    

    override func viewDidLoad() {
        super.viewDidLoad()
        self.setupUI()
        self.layoutUI()
        
        tableView.dataSource = self
        tableView.delegate = self
        
        let cell1 = CTableViewCell.init(style: .default, reuseIdentifier: "test")
        cell1.setup(title: "Advil", desc: "Before your meal", time: "11:30AM", image: #imageLiteral(resourceName: "Bitmap"))
        let cell2 = CTableViewCell.init(style: .default, reuseIdentifier: "test")
        cell2.setup(title: "Xanax", desc: "Before bed time", time: "9:15PM", image: #imageLiteral(resourceName: "noun_vertical_80648"))
        data = [cell1, cell2]
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.data.count
    }
    
    func tableView(_ tableView: UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]? {
       
        let refill = UITableViewRowAction(style: .normal, title: "Refill") { action, index in
            Alamofire.request("http://api.pillup.org/patient/2vziI7/medicine/0MWzgO/refill", method: .get)
        }
        
        refill.backgroundColor =  #colorLiteral(red: 0.3882352941, green: 0.631372549, blue: 0.7647058824, alpha: 1)
        
        let dispense = UITableViewRowAction(style: .normal, title: "Dispense") { action, index in
            Alamofire.request("http://api.pillup.org/patient/2vziI7/medicine/0MWzgO/dispense", method: .post)
            self.data.remove(at: index.row)
            tableView.reloadData()
        }
        
        dispense.backgroundColor =  #colorLiteral(red: 0.8039215686, green: 0.3294117647, blue: 0.2549019608, alpha: 1)
        return [dispense, refill]
        
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 80
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        return self.data[indexPath.row]
    }

}

extension ViewController {
    
    func setupUI() {
        
        self.tableView = UITableView()
        self.profileImageView = UIImageView()
        self.userNameLabel = UILabel()
        self.todayLabel = UILabel()
        self.myPillsLabel = UILabel()
        self.addButton = UIButton()
        self.myPillsLine = UIView()
//        self.chartView = BarChartView()
        
        self.view.backgroundColor = #colorLiteral(red: 0.9764705882, green: 0.9764705882, blue: 0.9764705882, alpha: 1)
        self.view.addSubview(tableView)
        self.view.addSubview(profileImageView)
        self.view.addSubview(userNameLabel)
        self.view.addSubview(todayLabel)
        self.view.addSubview(myPillsLabel)
        self.view.addSubview(addButton)
        self.view.addSubview(myPillsLine)
//        self.view.addSubview(chartView)
     
        
    }
    
    func layoutUI() {
        
        profileImageView.snp.makeConstraints { make in
            make.height.width.equalTo(32)
            make.top.equalToSuperview().offset(70)
            make.left.equalToSuperview().offset(35)
        }
        
        profileImageView.layer.masksToBounds = true
        profileImageView.layer.cornerRadius = 32 / 2
        profileImageView.image = #imageLiteral(resourceName: "Screen Shot 2018-09-16 at 3.03.54 AM")
        
        userNameLabel.snp.makeConstraints { make in
            make.centerY.equalTo(profileImageView)
            make.left.equalTo(profileImageView.snp.right).offset(8)
            make.width.equalTo(100)
        }
        
        userNameLabel.font = UIFont.systemFont(ofSize: 21, weight: .medium)
        userNameLabel.alpha = 0.9
        userNameLabel.text = "Shayan"
        
        todayLabel.snp.makeConstraints { make in
            make.left.equalToSuperview().offset(33)
            make.top.equalTo(profileImageView.snp.bottom).offset(20)
        }
        
        todayLabel.font = UIFont.systemFont(ofSize: 28, weight: .medium)
        todayLabel.alpha = 0.9
        todayLabel.text = "Today"
        
        tableView.snp.makeConstraints { make in
            make.left.right.equalToSuperview()
            make.top.equalTo(todayLabel.snp.bottom).offset(18)
            make.height.equalTo(284)
        }
        
        tableView.backgroundView?.backgroundColor = .clear
        tableView.backgroundColor = .clear
        
        myPillsLabel.snp.makeConstraints { make in
            make.left.equalTo(todayLabel.snp.left)
            make.top.equalTo(tableView.snp.bottom).offset(0)
        }
        
        myPillsLabel.font = UIFont.systemFont(ofSize: 28, weight: .medium)
        myPillsLabel.alpha = 0.9
        myPillsLabel.text = "My Pills"
        
        myPillsLine.snp.makeConstraints { make in
            make.left.right.equalToSuperview()
            make.height.equalTo(0.3)
            make.top.equalTo(myPillsLabel.snp.bottom).offset(12)
        }
        
        myPillsLine.alpha = 0.1
        myPillsLine.backgroundColor = #colorLiteral(red: 0.09803921569, green: 0.09803921569, blue: 0.09803921569, alpha: 1)
        
        let imageView = UIImageView()
        self.view.addSubview(imageView)
        imageView.image = #imageLiteral(resourceName: "Group 3")
        imageView.contentMode = .scaleAspectFit
        imageView.snp.makeConstraints { make in
            make.left.right.bottom.equalToSuperview().inset(20)
            make.top.equalTo(myPillsLine.snp.bottom).inset(-15)
        }
        
//        chartView.snp.makeConstraints { make in
//            make.centerX.equalToSuperview()
//            make.width.equalToSuperview().offset(-50)
//            make.bottom.equalToSuperview().offset(-20)
//            make.top.equalTo(self.myPillsLine.snp.bottom).inset(-20)
//        }
        
//        setChart()
//        chartView.scaleXEnabled = false
//        chartView.scaleYEnabled = false
//        chartView.drawGridBackgroundEnabled = false
//        chartView.xAxis.drawGridLinesEnabled = false
//        chartView.leftAxis.drawLabelsEnabled = false
//        chartView.rightAxis.drawLabelsEnabled = false
//        chartView.leftAxis.drawGridLinesEnabled = false
//        chartView.rightAxis.drawGridLinesEnabled = false
//
//        chartView.drawBordersEnabled = false
//        chartView.legend.enabled = false
//        //Change the background of the charts
////        chartView.drawBarShadowEnabled = true
//        chartView.drawBordersEnabled = false
//        chartView.minOffset = 0
//        chartView.borderColor = .clear
//        chartView.fitBars = false
//        chartView.leftAxis.axisMinimum = 0.0
//        chartView.rightAxis.axisMinimum = 0.0
//        chartView.maxVisibleCount = 0

    }
    
//    func setChart() {
//
//        let unitsSold = [10, 12]
//
//        let months = ["C1", "C2"]
//        let test = [1, 2]
//
//        var dataEntries: [BarChartDataEntry] = []
//
//        for i in 0 ..< months.count {
//            let dataEntry = BarChartDataEntry(x: Double(test[i]), y: Double(unitsSold[i]))
//
//            dataEntries.append(dataEntry)
//        }
//
//
//        let chartDataSet = BarChartDataSet(values: dataEntries, label: "Cartridge")
//        chartDataSet.drawValuesEnabled = false
//        chartDataSet.barBorderWidth = 0
//        chartDataSet.valueTextColor = .clear
//
//        chartDataSet.colors = [#colorLiteral(red: 0.2784313725, green: 0.8274509804, blue: 0.8196078431, alpha: 1), #colorLiteral(red: 0.9294117647, green: 0.08437372349, blue: 0.2941176471, alpha: 1)]
//        let chartData = BarChartData(dataSet: chartDataSet)
//
//        chartView.data = chartData
//    }
    

}
