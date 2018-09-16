//
//  ViewController.swift
//  PillUp
//
//  Created by Shayan on 9/16/18.
//  Copyright © 2018 Shayan. All rights reserved.
//

import UIKit
import SnapKit
import Charts

class ViewController: UIViewController {
    
    var tableView : UITableView!
    var profileImageView : UIImageView!
    var userNameLabel : UILabel!
    var todayLabel : UILabel!
    var myPillsLabel : UILabel!
    var addButton : UIButton!
    var myPillsLine : UIView!
    var chartView : BarChartView!
    

    override func viewDidLoad() {
        super.viewDidLoad()
        self.setupUI()
        self.layoutUI()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
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
        self.chartView = BarChartView()
        
        self.view.backgroundColor = #colorLiteral(red: 0.9764705882, green: 0.9764705882, blue: 0.9764705882, alpha: 1)
        self.view.addSubview(tableView)
        self.view.addSubview(profileImageView)
        self.view.addSubview(userNameLabel)
        self.view.addSubview(todayLabel)
        self.view.addSubview(myPillsLabel)
        self.view.addSubview(addButton)
        self.view.addSubview(myPillsLine)
        self.view.addSubview(chartView)
     
        
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
        
        myPillsLabel.snp.makeConstraints { make in
            make.left.equalTo(todayLabel.snp.left)
            make.top.equalTo(tableView.snp.bottom).offset(15)
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
        
        chartView.snp.makeConstraints { make in
            make.centerX.equalToSuperview()
            make.width.equalToSuperview().offset(-50)
            make.bottom.equalToSuperview().offset(-20)
            make.top.equalTo(self.myPillsLine.snp.bottom).inset(-20)
        }
        
        setChart()
        chartView.scaleXEnabled = false
        chartView.scaleYEnabled = false
        chartView.drawGridBackgroundEnabled = false
        chartView.xAxis.drawGridLinesEnabled = false
        chartView.leftAxis.drawLabelsEnabled = false
        chartView.rightAxis.drawLabelsEnabled = false
        chartView.leftAxis.drawGridLinesEnabled = false
        chartView.rightAxis.drawGridLinesEnabled = false

        chartView.drawBordersEnabled = false
        chartView.legend.enabled = false
        //Change the background of the charts
        chartView.drawBarShadowEnabled = true
        chartView.drawBordersEnabled = false
        chartView.minOffset = 0
        chartView.borderColor = .clear
        chartView.fitBars = false
        
        chartView.drawValueAboveBarEnabled = false
        
        YAxis.setAccessibilityElementsHidden(true)
        chartView.leftAxis.setValue(value: "23", forKeyPath: "1")


        
        
        chartView.chartDescription?.text = ""
//        lineChartData.setDrawValues(false)

        
        
       
    }


    func setChart() {
        
        let unitsSold = [10, 12, 3, 5]
        let months = ["", "", "", ""]
        let test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        
        var dataEntries: [BarChartDataEntry] = []
        
        for i in 0 ..< months.count {
            let dataEntry = BarChartDataEntry(x: Double(test[i]), y: Double(unitsSold[i]))
            
            dataEntries.append(dataEntry)
        }
        
        let chartDataSet = BarChartDataSet(values: dataEntries, label: " ")
        chartDataSet.colors = [#colorLiteral(red: 0.9019607843, green: 0.9215686275, blue: 0.1098039216, alpha: 1), #colorLiteral(red: 0.5058823529, green: 0.737254902, blue: 0.1490196078, alpha: 1), #colorLiteral(red: 0.2784313725, green: 0.8274509804, blue: 0.8196078431, alpha: 1), #colorLiteral(red: 0.9294117647, green: 0.08437372349, blue: 0.2941176471, alpha: 1)]
        let chartData = BarChartData(dataSet: chartDataSet)
        
        chartView.data = chartData
    }
    

}
