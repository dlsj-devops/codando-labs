package com.example.mailservice.services;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;

import org.jvnet.hk2.annotations.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;

@Service
public class ScheduleReportService {

    @Autowired
    private FileOSService fileOSService;

    @Autowired
    private EmailService emailService;

    private List<String> emailList = Arrays.asList("dlimapa@gmail.com");
    
    private final Integer SEVEN_DAYS_IN_MILISECONDS = 604800000;

    @Scheduled(fixedRate = 30000)
    public void sendReport() {
        System.out.println("Enviando email");
        try {
            String report = fileOSService.getReportFileContent("teste.hmtl");

            for (String email: emailList) {
                emailService.sendReport(report, email);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
}
